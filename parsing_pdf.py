#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from decimal import Decimal
import pdfplumber
from pdfplumber import utils
import pandas as pd
import uuid

TITLE_STYLE = [
    u"^(第[\d一二三四五六七八九十]+章、?).+",  # 0 例：第一章 XXX；第一章、XXX； 第一章.XXX；第1章 XXX；第1章、XXX； 第1章.XXX
    u"^(第[\d一二三四五六七八九十]+节、?).+",  # 1 例：第一节 XXX；第一节、XXX； 第一节.XXX；第1节 XXX；第1节、XXX； 第1节.XXX
    u"^(第[\d一二三四五六七八九十]+项、?(?!标准)).+",  # 2 例：第一项 XXX；第一项、XXX； 第一项.XXX；第1项 XXX；第1项、XXX； 第1项.XXX
    u"^(附注\s*[\d一二三四五六七八九十]+．?).+",  # 3 例：附注一；附注二
    u"^([一二三四五六七八九十]+[、\.]).+",  # 4 例：一、XXX
    u"^([\(（][一二三四五六七八九十]+[\)）](?!、)).+",  # 5 例：(一) XXX；（一） XXX
    u"^(注释\s*[\d一二三四五六七八九十]+[．\.、]?).+",  # 6 例：注释1；注释2
    u"^([\(（][一二三四五六七八九十]+[\)）]、).+",  # 7 例：(一) 、XXX；（一）、XXX
    u"^(\d{1,2}、).+",  # 8 例：1、XXX    与7例的位置进行了调换  公司：永力达
    u"^(\d{1,2}[\.．](?!\d{1,3}\D+|\d{1,2}(?=20[1-5]\d))).+",  # 9 例：1.XXX
    u"^([1-4]?\d(?![kK][wW]|号|名|世纪|%|年以[内上]|年[至到]|年|）|\)|\.|．)(?=\D{2,})).+",  # 10 例：1XXX
    u"^(\d{1,2}[\.．]\d{1,2}(?:[\.．](?!\d{1,3}\D)|(?=\D{2,})|(?=20[1-5]\d))).+",
    # 11 例：1.1 XXX；1.1.XXX  （注意：1.2017年11月27日，海口市制药厂有限公司被海南省科技厅）
    u"^(\d{1,2}[\.．]\d{1,2}[\.．]\d{1,2}(?:[\.．](?!\d{1,3}\D)|(?=\D{2,}))).+",  # 12 例：1.1.1 XXX；1.1.1.XXX
    u"^(\d{1,2}[\.．]\d{1,2}[\.．]\d{1,2}[\.．]\d{1,2}(?:[\.．](?!\d{1,3}\D)|(?=\D{2,}))).+",
    # 13 例：1.1.1.1 XXX；1.1.1.1.XXX
    u"^([\(（]\d{1,2}[\)）](?!、|=)).+",  # 14 例：(1) XXX；（1） XXX
    u"^([\(（]\d{1,2}[\)）]、).+",  # 15 例：(1)、XXX；（1）、XXX
    u"^((?<!\(|（)\d+[\)）]).+",  # 16 例：1) XXX；1） XXX
    # 修正BUG #16264，错误将“T.I.S. Service S.P.A”识别为标题
    # 修正BUG #17569，错误将“S日为关注日”和“V为本期债券质押率”识别为标题
    u"^([a-zA-Z](?=[\.．、]?\s?(?!为|日为|系列)(?:[\u4e00-\u9fa5]))).+",  # 17 例：A XXX；a XXX；A.XXX；a.XXX
    u"^([①②③④⑤⑥⑦⑧⑨⑩]、?).+"  # 18 例：① XXX
]


class ParsingPdf:

    def __init__(self):
        self.title_pattern = "|".join(TITLE_STYLE)  # 初始化标题判断正则表达式

    @staticmethod
    def relation(interval1, interval2):
        """
        @msg: 判断两个区间的关系
        @param interval1 {list} 第一个区间
        @param interval2 {list} 第二个区间
        @return: {int}  返回两个区间的关系，0:两个区间相等、1:两个区间相离、2:两个区间相交、3:两个区间为包含关系
        """
        min1, max1 = sorted(interval1)
        min2, max2 = sorted(interval2)
        if min1 == min2 and max1 == max2: return 0
        if max1 < min2 or max2 < min1: return 1
        if min1 < min2 <= max1 < max2 or min2 < min1 <= max2 < max1: return 2
        if min1 <= min2 <= max2 <= max1 or min2 <= min1 <= max1 <= max2: return 3

    def reset_cols(self, row_line_list, rows):
        last_cols = row_line_list[-2]
        cur_cols = row_line_list[-1]
        last_txt_cols = rows[-2]
        if len(last_cols) < len(cur_cols):
            mixed_list = [""] * len(cur_cols)
            for i, col in enumerate(cur_cols):
                x0, x1 = col.get("x0"), col.get("x1")
                for l_col in last_cols:
                    l_x0, l_x1 = l_col.get("x0"), l_col.get("x1")
                    if self.relation([x0, x1], [l_x0, l_x1]) in [2, 3]:
                        mixed_list[i] = 1
            for k, res in enumerate(mixed_list):
                if res == "":
                    last_cols.insert(k, {})
                    last_txt_cols.insert(k, "")
        elif len(last_cols) > len(cur_cols):
            for i, l_col in enumerate(last_cols):
                for col in cur_cols:
                    if col.get("x0") == l_col.get("x0") and i > 0:
                        last_txt_cols[i] = last_txt_cols[i] + "\n" + col.get("text")
                        break
                last_cols[i] = cur_cols

    @staticmethod
    def get_header(pages):
        header = []
        page1_header_words = pages[0].extract_words()[0:3]
        page2_header_words = pages[1].extract_words()[0:3]
        page3_header_words = pages[2].extract_words()[0:3]
        for i, word in enumerate(page1_header_words):
            if word.get("text") == page2_header_words[i].get("text") and word.get("text") == page3_header_words[i].get(
                "text"):
                header.append(word.get("text"))

        page1_header_words = pages[-1].extract_words()[0:3]
        page2_header_words = pages[-2].extract_words()[0:3]
        page3_header_words = pages[-3].extract_words()[0:3]
        for i, word in enumerate(page1_header_words):
            if word.get("text") == page2_header_words[i].get("text") and word.get("text") == page3_header_words[i].get(
                "text"):
                header.append(word.get("text"))
        return header

    @staticmethod
    def filter_header(word, header, page_width):
        my_top = word.get("top")
        # my_x1 = word.get("x1")  or str(word.get("text")).isdigit() and (my_x1/page_width - Decimal('0.5')) < 0.1
        is_filter = (word.get("text") in header and my_top < 80)
        return is_filter

    def start(self, path):
        line_list, paragraph_list, table_list, header, col_line_list, row_line_list, cols, rows = [], [], [], [], [], [], [], []
        with pdfplumber.open(path) as pdf:
            header = self.get_header(pdf.pages)
            first_page = pdf.pages[36]
            # 将页面的所有字符对象整理到一个字符串中。添加x1一个字符的字符与下一个字符的字符之间的差x0大于的空格x_tolerance。添加换行符doctop，其中一个字符的字符与下一个字符的字符之间的差doctop大于y_tolerance
            first_page.extract_text()
            # rects = first_page.within_bbox()
            page_width = first_page.width
            print("width:", first_page.width)
            print("height:", first_page.height)
            im = first_page.to_image(resolution=300)
            bbox1 = (Decimal('50.66'), Decimal('249.819'), Decimal('245.420'), Decimal('255.379'))
            result = first_page.within_bbox(bbox1)  # 裁剪坐标内的文本
            print(result)
            # print(first_page.extract_words()[0])
            im.draw_rect(bbox1, stroke_width=1)
            im.save("D:\\a.png", format="PNG")
            # exit()
            # print(first_page.lines)
            # print(first_page.objects.get("line", ''))
            line_dict, table_pos = {}, []
            table_lines = {}
            table_line_in = False
            # align_list, align = [], {}
            words = first_page.extract_words()
            l_x0, l_x1, l_top, bottom, line_width, line, paragraph = 0, 0, 0, 0, 0, "", ""
            x_max, x_min = 0, 0
            cell_list = []
            for index, word in enumerate(list(words)):
                word['id'] = str(uuid.uuid1())
                word_text = word.get("text")
                if self.filter_header(word, header, page_width):  # 页码和表头退出
                    continue
                # l_top: 上一个word的top值
                # 当前的wod的top值和上一个word的top差值小于2，说明就在同一行
                if (word.get("top") - l_top) < 2 or l_x0 == 0:  # 拼接同一行的数据
                    # x0：word的最小left值，
                    # l_x1：上一个word的最大left值，即word.left + word.width
                    # word.get("x0") 当前word的left值
                    is_need_blank = bool(re.search("^[A-Za-z]+$", word_text) or (word.get("x0") - l_x1) / 2 > 7 and l_x1 > 0)
                    line = line + (" " if is_need_blank else "") + word_text
                    line_width = line_width + (
                        word.get("x1") - word.get("x0"))  # (word.get("x1") - word.get("x0")) 计算当前word的width
                    if l_x0 == 0:
                        line_dict.update({"x0": word.get("x0")})
                else:
                    if len(line) > 0:
                        line_dict.update({"x1": l_x1, "line": line, "line_width": line_width})
                        line_list.append(line_dict)
                    line_dict = {}
                    line_dict.update({"x0": word.get("x0")})
                    line = word_text
                    line_width = (word.get("x1") - word.get("x0"))
                l_x0 = word.get("x0")
                l_x1 = word.get("x1")
                l_top = word.get("top")
                bottom = word.get("bottom")

                pre_word = words[index - 1]
                pre_x0 = pre_word.get("x0")
                pre_x1 = pre_word.get("x1")
                pre_top = pre_word.get("top")
                if (word.get("top") - pre_top) < 2 and not re.search(self.title_pattern, line) and not table_line_in:  # 拼接同一行的数据
                    if word.get("x0") - pre_x1 > 15:  # 表格行的处理，word之间间隔大于15就当表格处理
                        table_line_in = True
                        if len(cell_list):
                            print(cell_list, x_max, x_min)
                        if word.get('x0') > x_max:
                            x_max = word.get('x0')
                        if word.get('x0') < x_min:
                            x_min = word.get('x0')
                        table_lines.update({word.get("top"): [words[index - 1], word]})  # 当前值和左边值
                        if not len(cell_list):
                            x_max = pre_x0
                            x_min = pre_x0
                            cell_list.append(pre_word)
                        cell_list.append(word)
                elif table_line_in and word.get("top") - pre_top <= 20:
                    col_list = table_lines.get(word.get("top"), '')  # 同一行的数据
                    cell_list.append(word)
                    if word.get('x0') > x_max:
                        x_max = word.get('x0')
                    if word.get('x0') < x_min:
                        x_min = word.get('x0')
                    if col_list:
                        col_index = len(col_list) + 1
                        pre_key = list(table_lines.keys())[-2]
                        pre_col_list = table_lines.get(pre_key)
                        if tmp_word.get("x0") > word.get("x1"):  # tmp_word 距离最近的数据
                            pre_col_list.insert(len(col_list), {})
                        elif tmp_word.get("x1") < word.get("x0"):
                            pre_col_list.insert(len(col_list) + 1, {})  # col_list：和当前word同一水平的全部数据
                        col_list.append(word)
                        table_lines.update({word.get("top"): col_list})
                    else:
                        pre_key = list(table_lines.keys())[-1]
                        pre_col_list = table_lines.get(pre_key)
                        tmp_word = pre_col_list[0]  # 倒着读的，所以要取最左边的数据
                        # if relation([tmp_word.get("x0"), tmp_word.get("x1")], [word.get("x0"), word.get("x1")]) == 1:
                        if tmp_word.get("x0") > word.get("x1"):
                            pre_col_list.insert(0, {})
                        elif tmp_word.get("x1") < word.get("x0"):
                            pre_col_list.insert(1, {})
                        table_lines.update({word.get("top"): [word]})
                elif word.get("top") - pre_top > 20:
                    table_line_in = False

if __name__ == '__main__':
    main = ParsingPdf()
    path = u'test.pdf'
    main.start(path)
