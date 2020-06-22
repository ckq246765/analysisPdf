#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import datetime
from typing import Set
from flask_cors import CORS
from bs4 import BeautifulSoup
from decimal import Decimal
from util_base.util import util
from flask import Flask


class AnalyzeTable(object):

    def __init__(self):
        self.style_content = ''
        self.doc_dict = []
        self.row = []
        self.rows = []
        self.is_table = False
        self.table_name = ''
        self.page_width = ''
        self.footer_values = set()
        self.exclude_list = []

    def save_el_style(self, soup):
        content = []
        style = soup.find_all('style')
        for sty in style:
            content += sty.contents
        self.style_content = ''.join(content)

    def exclude_elem(self, elem, index, _class):
        in_text = re.sub(' ', '', elem.text)
        left_cls, is_f_h = '', False
        for item in _class:
            if re.search('^x', item):
                left_cls = item
            if re.search('^m', item):
                is_f_h = True
        if is_f_h and left_cls:
            style_dict = self.get_elem_style([left_cls])
            if style_dict.__contains__('x') and style_dict['x']:
                left, text = style_dict['x'], re.sub(' ', '', elem.text)
                if self.page_width and (self.page_width - left) <= 5 and text.isdigit():
                    return True

        if index == 1 and re.search('公告编号', in_text):
            return True
        if (index == 0 and elem.name == 'img') or elem.name == 'a':  # img标签和a标签不解析
            return True

        if len(in_text) < 3 and re.fullmatch('\d', in_text):  # 一般是页码数，不处理
            return True
        return False

    @staticmethod
    def get_elem_type(_class):
        for index, item in enumerate(_class):
            if re.search('^h', item):
                if index != len(_class) - 1:
                    return item, 'p'
                else:
                    return item, 'table'
        return '', ''

    def format_style(self, cls):
        match = re.search('\.' + cls + '\{.*px;\}', self.style_content)
        if match:
            style = match.group()
            style = re.sub(' ', '', style)
            val = re.findall('(?<=:).*(?=p)', style)
            return Decimal(val[0])
        return ''

    def save_first_child_text(self, elem):
        """
        将前几个的dom的内容缓存起来，如果每页都有出现，那么就当做是也没处理
        @param elem:
        @return:
        """
        if elem.text in self.footer_values:
            return True

        if elem.text:
            self.footer_values.add(elem.text)
            return False

    def get_elem_style(self, _class):
        """
        @param: x h y fs: left height bottom font-size
        @return: x h y fs对应的值
        """
        style_dict = {}
        for cls in _class:
            match = re.search('^[xhyw]|^fs', cls)
            if match:
                match_val = match.group()
                css = self.format_style(cls)
                style_dict[match_val] = css
                if style_dict.__contains__('x') and style_dict.__contains__('w'):
                    style_dict['r'] = style_dict['x'] + style_dict['w']
        return style_dict

    def get_page_width(self, elem):
        """
        获取page的宽度，在排除页脚的时候使用
        @param elem:
        @return:
        """
        if not self.page_width:
            page_class = elem.attrs['class']
            style_dict = self.get_elem_style(page_class)
            if style_dict.__contains__('w'):
                self.page_width = style_dict['w']

    def start(self):
        start = datetime.datetime.now()
        soup = BeautifulSoup(open('test.p.html', encoding='utf-8'), features='html.parser')
        self.save_el_style(soup)
        contents = soup.find_all('div', id=re.compile('^(pf).*[\d|[a-zA-Z]'))  # 获取page
        if len(contents):
            for con_index, content in enumerate(contents):
                if con_index in [105, 106, 107]:  # con_index in [36, 37] in [103]:  # con_index in [103]
                    children = content.contents[0].contents  # 只取第一层子集
                    first_child = False
                    self.get_page_width(content)
                    print('-----------------page------------------', con_index + 1)
                    for index, item in enumerate(children):
                        _class = item.attrs['class'][1:]
                        if index < 4:
                            if self.save_first_child_text(item):
                                continue

                        if item.name == 'div' and first_child is False:  # 页眉不读
                            first_child = True
                            continue

                        if not self.is_table and self.exclude_elem(item, index, _class):
                            continue
                        self.process_element(_class, item)

            self.check_end()

    @staticmethod
    def exclude_table_name(sentence):
        value_pattern = u"((?<![^\(（\s])单位(?!情况)|单位(?=:|：)|(?<!\S)单元|(?<!的|及|和|\S)(?<!单项|款项|账面)金额)|（除特别注明外，金额单位均为(?:人民币)元）"
        return bool(re.search(value_pattern, sentence))

    @staticmethod
    def is_same_line(current_style, row):
        if not len(row):
            return True
        last_cell = row[-1]
        if current_style:
            # if last_cell['pos']['y'] != current_style['y']:
            #     return False
            if last_cell['pos']['x'] > current_style['x']:
                return False
        return True

    @staticmethod
    def is_row_line(current_style, row, rows):
        """
            是否是同一行
            通过判断每个单元格的right值来确定是否是新的一行
        """
        if len(rows):
            if len(row) > 1:
                prev_style = row[len(row) - 2]['pos']
                if current_style['r'] < prev_style['r']:
                    return True
        return False

    @staticmethod
    def _get_col_val(row):
        result = []
        for col in row:
            result.append(col['text'])
        _result = list(set(result))
        _result.sort(key=result.index)
        return ''.join(_result)

    @staticmethod
    def row_have_value(row):
        result = []
        for col in row:
            text = col['text']
            if text:
                result.append(text)
        return bool(len(result))

    @staticmethod
    def col_is_pgh(row):
        """ 如果row中的所有col的值都一样，那就当做是段落来处理 """
        col_values = set()
        for col in row:
            col_values.add(col['text'])
        return bool(len(col_values) == 1)

    def format_table(self, tmp_index, table_data):
        """ 将段落和表格拆分出来 """
        n, doc_dict, result_row, table_name = 0, [], [], ''
        while n < len(table_data):
            table_row = table_data[n]
            row_inner = self._get_col_val(table_row)
            if row_inner and (util.check_is_title(row_inner) or self.col_is_pgh(table_row)):
                if len(result_row):
                    pos = table_row[0]['pos']
                    pgh_dict = {
                        'el_type': 'p',
                        'text': row_inner,
                        'style_dict': pos
                    }
                    self.doc_dict.insert(tmp_index + 1, pgh_dict)
                    pass
                table_data.pop(n)
                continue

            if self.row_have_value(table_row):
                result_row.append(table_row)
            else:
                table_data.pop(n)
                continue

            n += 1

    def get_table_name(self, doc_dict={}):
        doc_dict = doc_dict if doc_dict else self.doc_dict
        n = len(doc_dict) - 1
        table_name = ''
        while n > 0:
            temp_dict = doc_dict[n]
            text = temp_dict['text']
            if self.exclude_table_name(text):
                n -= 1
                continue
            else:
                table_name = text
                break
        return util.del_the_sequence(table_name)

    def process_element(self, _class, item):
        pass

    def check_end(self):
        pass


class ProcessTable(AnalyzeTable):

    def __init__(self):
        super(ProcessTable, self).__init__()

    def process_element(self, _class, elem):
        """
       @msg: 解析元素
       @param _class：当前元素的class，
       @param 段落的class一般为[m0 x3 h21 y148 ff2 fs2 fc0 sc1 ls0 ws0]，其中h21中的h表示元素的高度，后面的数字越大则元素的高度越高
       @param 单元格的class一般为[x21 y140 w24 h42]
       @param elem：当前元素
       """
        class_name, elem_type = self.get_elem_type(_class)
        if class_name and elem_type:
            text = re.sub(' ', '', elem.text)
            style_dict = self.get_elem_style(_class)
            # 存之前判断是否是同一段落的
            if elem_type == 'p':
                self.save_pgh(elem_type, text, style_dict)

            if elem_type == 'table':
                self.save_table(style_dict, text)

    def merge_table_data(self):
        last_child = self.doc_dict[-1]
        if last_child['el_type'] == 'table':
            if (last_child['table_name'] == '' and self.table_name == '') or (last_child['table_name'] == self.table_name):
                last_child['table_data'] += self.rows
                self.rows = []
                return True
        return False

    def save_pgh(self, elem_type, text, style_dict):
        if self.is_table:
            if not self.merge_table_data():
                self.doc_dict.append({
                    'el_type': 'table',
                    'text': '',
                    'table_name': self.table_name,
                    'table_data': self.rows,
                    'style_dict': style_dict
                })
            self.is_table, self.rows, self.table_name = False, [], ''
            return False

        self.doc_dict.append({
            'el_type': elem_type,
            'text': text,
            'table_name': '',
            'style_dict': style_dict
        })

    def save_table(self, style_dict, text):
        self.is_table = True
        # 单元可以根据bottom的值来判断是不是同一行
        if not self.table_name:
            self.table_name = self.get_table_name()
        temp_dict = {'pos': style_dict, 'text': text}
        if self.is_same_line(style_dict, self.row) and not self.is_row_line(style_dict, self.row, self.rows):
            self.row.append(temp_dict)
        else:
            self.rows.append(self.row)
            self.row = [temp_dict]

    def check_end(self):
        self.merge_table_data()
        self.process_table()

    def process_table(self):
        for index, tmp in enumerate(self.doc_dict):
            if tmp['el_type'] == 'table':
                self.format_table(index, tmp['table_data'])
        print(self.doc_dict)




if __name__ == '__main__':
    process = ProcessTable()
    process.start()
