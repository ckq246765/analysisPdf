#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json


class Util:
    PARAGRAPH_PRE_SUB = u"“|^\*?注：|^.{0,3}说明："
    DATE_REPLACE_PATTERN = u"20\d{2}\D[01]?\d\D[0-3]?\d(?!\d)"
    SPECIAL_PGH_HEAD_NOT_TITLE = "^[2345]G|^\d{1,2}个?月|^\d+(?!\d?[\.．、\)）]).*(?:利息|借款|应付款)|^\d+(\.\d+)?[百千万]|\d+-?—?\d+?岁|^\d{5,}|^\d亿|\d(?:SPH|位自然人)|X射线"
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
    def __init__(self):
        self.title_pattern = "|".join(self.TITLE_STYLE)

    @staticmethod
    def doc_replace(sentence):
        return sentence.replace("\r", "").replace("\x01", "").replace("\t", "").replace("\xa0", "").replace("\n",
                                                                                                            "\x07",
                                                                                                            "").replace(
            "\x02", "").replace("\x0c", "").replace("\x0e", "").replace("\u3000", "").replace("\u200D", "").replace(
            "\u0007", "").replace("\x0b", "").strip()

    @staticmethod
    def chinese_to_int(china_number):
        common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8,
                                    '九': 9, '十': 10}
        total = 0
        r = 1  # 表示单位：个十百千...
        for i in range(len(china_number) - 1, -1, -1):
            val = common_used_numerals_tmp.get(china_number[i])
            if val == None:
                return china_number
            if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
                if val > r:
                    r = val
                    total = total + val
                else:
                    r = r * val
            elif val >= 10:
                r = val if val > r else r * val
            else:
                total = total + r * val
        return total

    # 将“①②③④⑤⑥⑦⑧⑨⑩”转换为整型数字
    @staticmethod
    def circle_to_int(circle_number):
        CIRCLE_NUM = {'①': 1, '②': 2, '③': 3, '④': 4, '⑤': 5, '⑥': 6, '⑦': 7, '⑧': 8, '⑨': 9, '⑩': 10}
        return CIRCLE_NUM[circle_number]

    def get_title_number(self, title_sytle_num, sequence):
        # 类似“1.1.XXX”和“1.1.1.XXX”因为难以数字化，所以暂时不处理
        if title_sytle_num not in self.NOT_CHECK_TITLE_NUMBER_LIST:
            number_str = re.findall(u"([\d一二三四五六七八九十①②③④⑤⑥⑦⑧⑨⑩a-zA-Z]+)", Base.doc_replace(sequence))[0]
            if re.match("^\d+$", number_str):
                return int(number_str)
            elif re.match("^[一二三四五六七八九十]+$", number_str):
                return self.chinese_to_int(number_str)
            elif re.match("^[①②③④⑤⑥⑦⑧⑨⑩]+$", number_str):
                return self.circle_to_int(number_str)
            elif re.match("^[a-zA-Z]+$", number_str):
                return self.letter_to_int(number_str)
        return 1

    def get_style_info(self, paragraph_text, pgh_id=""):
        dict_style = dict()
        paragraph_text = re.sub(" ", "", paragraph_text)
        try:
            if self.check_is_title(paragraph_text):
                paragraph_text = self.doc_replace(paragraph_text)
                pgh_text_processed = re.sub(self.PARAGRAPH_PRE_SUB, "", paragraph_text)
                pgh_text_processed_date_replaced = re.sub(self.DATE_REPLACE_PATTERN, "@替换日期@", pgh_text_processed)
                find_tuple_list = re.findall(self.title_pattern, pgh_text_processed_date_replaced)
                if find_tuple_list:
                    find_tuple = find_tuple_list[0]
                    sequence_str = list(filter(lambda x: bool(x), find_tuple))[0]  # 过滤掉空字符串并拿到第一个非空字符串
                    type_num_result = find_tuple.index(sequence_str)
                    content_str = pgh_text_processed.split(sequence_str, 1)[-1]
                    content_str = re.sub('\.',"", content_str)  # BUG #16497  去掉 小数点
                    content_str = content_str.strip()
                    title_number = self.get_title_number(type_num_result, sequence_str)
                    # num:标题样式特征值，也是标题预设等级；sequence:标题序号（如标题“1、XXX”中的“1、”）； index:标题内容（如标题“1、XXX”中的“XXX”）
                    dict_style = {'title_style_num': type_num_result, 'sequence': sequence_str, 'index': content_str,
                                  "title_id": pgh_id, "title_text": paragraph_text, "title_level": "", "title_number": title_number, "title_pid": ""}
        except Exception as e:
            print(e)
            pass
        return dict_style

    def check_is_title(self, paragraph_text):
        if re.search(self.SPECIAL_PGH_HEAD_NOT_TITLE, re.sub(" ", "", paragraph_text)):
            return False
        pgh_text_processed = re.sub(self.PARAGRAPH_PRE_SUB, "", paragraph_text)
        pgh_text_processed = self.doc_replace(pgh_text_processed)
        pgh_text_processed = re.sub(self.DATE_REPLACE_PATTERN, "@替换日期@", pgh_text_processed)
        find_list = re.findall(self.title_pattern, pgh_text_processed)
        return bool(find_list)  # and len(paragraph_text) < self.MAX_TITLE_LENGTH

util = Util()
