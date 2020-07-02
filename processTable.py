#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import datetime
from typing import Set
from bs4 import BeautifulSoup
from decimal import Decimal

from util_base.util import util
from flask_cors import CORS
from flask import Flask
import subprocess

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/process')
def main():
    return {
        "data": json.dumps(ProcessTable().start(), ensure_ascii=False, cls=DecimalEncoder)
    }


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


class AnalyzeTable(object):
    EXCLUDE_TABLE_NAME = u"(?<![^\(（\s])单位(?!情况)|单位(?=:|：)|(?<!\S)单元|" \
                         u"调整情况说明.*：.*详见|" \
                         u"（除特别注明外，金额单位均为(?:人民币)元）|.*表$|.*表(（续）)$"

    def __init__(self):
        self.first_child = False
        self.header_elem = False
        self.style_content = ''
        self.doc_dict = []
        self.row = []
        self.rows = []
        self.is_table = False
        self.table_name = ''
        self.page_width = ''
        self.util = util
        self.page_rect = {}
        self.footer_values = set()
        self.exclude_list = []
        self.recursion_elem_contents = []

    def save_el_style(self, soup):
        content = []
        style = soup.find_all('style')
        for sty in style:
            content += sty.contents
        self.style_content = ''.join(content)

    @staticmethod
    def exclude_table_val(_class):
        last_class = _class[-1:][0]
        return bool(re.search('^h', last_class))

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
                if self.page_width and (self.page_width - left) <= 5 and text.isdigit():  # 一般是页码数，不处理
                    return True

        if index == 1 and re.search('公告编号', in_text):
            return True

        if index == 0 and elem.name == 'img':  # img标签和a标签不解析  or elem.name == 'a'
            return True

        if self.header_elem is False:
            self.header_elem = True
            return True
        #
        # if len(in_text) < 3 and re.fullmatch('\d', in_text):  # 一般是页码数，不处理
        #     return True
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
        将前几个的dom的内容缓存起来，如果每页都有出现，那么就当做是页眉处理
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
        style_dict = {
            'x': Decimal(0),
            'w': Decimal(0),
            'y': Decimal(0),
            'r': Decimal(0),
            'fs': Decimal(0)
        }
        for cls in _class:
            match = re.search('^[xhyw]|^fs', cls)
            if match:
                match_val = match.group()
                css = self.format_style(cls)
                style_dict[match_val] = css
                if style_dict.__contains__('x') and style_dict.__contains__('w'):
                    style_dict['r'] = style_dict['x'] + style_dict['w']
        return style_dict

    def get_page_rect(self, elem):
        """
        获取page的宽度，在排除页脚的时候使用
        @param elem:
        @return:
        """
        if not self.page_rect:
            page_class = elem.attrs['class']
            style_dict = self.get_elem_style(page_class)
            if style_dict.__contains__('w'):
                self.page_rect = style_dict

    @staticmethod
    def get_elem_node_name(els):
        node_names = set()
        for el in els:
            node_names.add(el.name)
        return node_names

    def recursion_elem(self, item, index):
        _class = item.attrs['class'][1:]
        c_children = item.contents
        print('-------text----------', item.text)
        node_names = self.get_elem_node_name(c_children)
        style_dict = self.get_elem_style(_class)
        if self.exclude_elem(item, index, _class):
            return True

        # len(list(item.contents)) > 2 and len(list(node_names)) == 1 and list(node_names)[0] == 'div'
        if abs(style_dict.__contains__('h') and style_dict['h'] - self.page_rect['h']) <= 5:
            self.recursion_elem_contents = item.contents

        if len(self.recursion_elem_contents):
            return self.loop_child_elem(self.recursion_elem_contents)
        self.process_element(_class, item, index)

    def loop_child_elem(self, children):
        for index, item in enumerate(children):
            self.recursion_elem_contents = []
            self.recursion_elem(item, index)

    def start(self):
        start = datetime.datetime.now()
        soup = BeautifulSoup(open('out/873280_秦燕科技_2019年_.html', encoding='utf-8'), features='html.parser')
        self.save_el_style(soup)
        contents = soup.find_all('div', id=re.compile('^(pf).*[\d|[a-zA-Z]'))  # 获取page
        if len(contents):
            for con_index, content in enumerate(contents):
                self.page_rect = {}
                if con_index in [38, 39, 40, 41]:  # con_index in [53, 54, 55]:  # con_index in [21, 22, 23]
                    children = content.contents[0].contents  # 只取第一层子集
                    self.get_page_rect(content)
                    self.header_elem = False
                    print('-----------------page------------------', con_index + 1)
                    self.loop_child_elem(children)
            self.check_end()
            end = datetime.datetime.now()
            print("文档IO用时：" + str((end - start).seconds) + u"秒")
            return json.dumps(self.doc_dict, ensure_ascii=False, cls=DecimalEncoder)

    @staticmethod
    def exclude_table_name(sentence):
        value_pattern = u"((?<![^\(（\s])单位(?!情况)|单位(?=:|：)|(?<!\S)单元|(?<!的|及|和|\S)(?<!单项|款项|账面)金额)|" \
                        u"（除特别注明外，金额单位均为(?:人民币)元）|□不适用|√|编制单位[﹕:：]|" \
                        u"是 ?√|^（续|^续）|^续：|^(（续）)|^(（续上表）)|^续表|^续上表|接上表|√ ?适用|" \
                        u"上期金额|本期金额|法定代表人.*会计机构负责人|^\(续\)[﹕:：]|||||\(*?适用|([\(|□||]*?适用)|" \
                        u"[\(|（]收益以.*?列示[）|\)]|[\(|（]续表[）|\)]"
        return bool(re.search(value_pattern, sentence))

    @staticmethod
    def is_same_line(current_style, row):
        if not len(row):
            return True
        last_cell = row[-1]
        if current_style:
            # if last_cell['pos']['y'] != current_style['y']:
            #     return False
            if last_cell['pos']['r'] > current_style['r']:
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
            try:
                if col['text']:
                    result.append(col['text'])
            except Exception as e:
                print(e)
        _result = list(set(result))
        _result.sort(key=result.index)
        return result, ''.join(_result)

    @staticmethod
    def row_have_value(row):
        result = []
        for col in row:
            text = col['text']
            if text:
                result.append(text)
        return bool(len(result))

    def col_is_pgh(self, row, row_inner, table_data, n):
        """ 如果row中的所有col的值都一样，那就当做是段落来处理 """
        # 按组合计提坏账准备：|按单项计提坏账准备：|
        if n > 0:
            prev_row = table_data[n - 1]
            _has_total = False
            for col in prev_row:
                if re.search('^(合计)|^(总计)', col['text']):
                    _has_total = True
                    break

            if _has_total:
                cols_val_result, cols_val = self._get_col_val(row)
                if len(cols_val_result) > 1:
                    return False
                return bool(len(prev_row) > len(row))

        if re.search('.*(的情况：)$|(涉及政府补助的项目：)$', row_inner):  # 存在不同企业所得税税率纳税主体的情况：
            return True

        col_values = set()
        n_empty_col_values = []

        if len(row) > 1:
            for col in row:
                text = col['text']
                if text:
                    n_empty_col_values.append(text)
                col_values.add(text)
            if len(col_values) < 3 and len(set(n_empty_col_values)) == 1:
                return True
        return bool(len(col_values) == 1) or bool(len(set(n_empty_col_values)) == 1 and len(n_empty_col_values[0]) > 20)

    def get_inner_char_num(self, doc_dict_index):
        if len(self.doc_dict) < 2:
            return True

        table_name = self.doc_dict[doc_dict_index]['table_name']

        title_info = self.util.get_style_info(table_name)
        if re.search('.*(情况|分析[:：]?)$', table_name):  # 控股股东情况
            return False

        if re.search('(商业模式|变动原因|经营计划|行业情况|风险因素|不确定性因素|经营计划或目标|公司发展战略|行业发展趋势|研发项目情况).{0,3}[:：]?$', table_name):
            return False

        if title_info:
            return True

        return False

    def check_row_is_title(self, row_inner, row, table_data, n):
        """
        校验带标题的单元格是否是段落，如：非经常性损益表——秦燕科技
        @param row_inner:
        @param row:
        @param table_data:
        @param n:
        @return:
        """
        title_info = self.util.check_is_title(row_inner)
        if title_info:
            prev_row, next_row = {}, {}
            if len(table_data) > n:
                ''' 如果行大于0，则根据之前行的去做对比 '''
                if n > 0:
                    prev_row = table_data[n - 1]

                if len(table_data) > n + 1:
                    next_row = table_data[n + 1]

                current_col_pos, current_col_index = {}, None
                for index, col in enumerate(row):
                    if re.search(col['text'], row_inner):
                        current_col_index, current_col_pos = index, col['pos']
                        break

                prev_bool, next_bool = True, True
                if current_col_pos and prev_row:
                    prev_pos = prev_row[current_col_index]['pos']
                    if prev_pos['w'] == current_col_pos['w'] and prev_pos['x'] == current_col_pos['x']:
                        prev_bool = False

                if current_col_pos and next_row:
                    next_pos = next_row[current_col_index]['pos']
                    if next_pos['w'] == current_col_pos['w'] and next_pos['x'] == current_col_pos['x']:
                        next_bool = False

                if prev_bool and next_bool:
                    return True
        return False

    def check_row_has_total(self, row, table_data, n):
        if n > 0:
            prev_row = table_data[n - 1]
            _has_total = False
            for col in prev_row:
                if re.search('^(合计)|^(总计)', col['text']):
                    _has_total = True
                    break
            if _has_total:
                cols_val_result, cols_val = self._get_col_val(row)
                if len(cols_val_result) > 1:
                    return False
                return bool(len(prev_row) > len(row))

    def check_other_row_name(self, row_inner, row, tmp_index):
        if re.search('.*(的情况：)$|(涉及政府补助的项目：)$', row_inner):  # 存在不同企业所得税税率纳税主体的情况：
            return True

        if re.search('\d{4}年\d{1,2}月.*计提.*(账款)$', row_inner):  # 先加一些规则来判断 P127
            return True

        if len(row) <= 2:
            col_width = []
            col_vals = set()
            for col in row:
                col_width.append(col['pos']['w'])
                if col['text']:
                    col_vals.add(col['text'])
            col_max_width = max(col_width)
            if len(col_vals) < 2 and self.get_inner_char_num(tmp_index) and col_max_width > 300:
                return True

    def row_name_is_paragraph(self, row_inner, row, table_data, n, tmp_index):
        if self.get_inner_char_num(tmp_index):
            return True

        # if self.check_row_is_title(row_inner, row, table_data, n):
        #     return True

        if self.check_row_has_total(row, table_data, n):
            return True

        if self.check_other_row_name(row_inner, row, tmp_index):
            return True

        return False

    @staticmethod
    def check_col_pos(col, s_col):
        """ 单元格的宽和left值会有丁点的误差 """
        return bool(abs(col['pos']['w'] - s_col['pos']['w']) <= 2) and (abs(col['pos']['x'] - s_col['pos']['x']) <= 2)
        # return bool(col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x'])

    @staticmethod
    def get_max_row_len(rows):
        row_lens_arr = []
        for index, item in enumerate(rows):
            row_lens_arr.append(len(item))
        return row_lens_arr

    @staticmethod
    def demerge_col(col_width, standard_row, col_index):
        """
        拆分单元格
        @param col_width: 当前列的宽度
        @param standard_row: 标准行
        @param col_index: 标准行 列的索引
        @return:
        """
        sum_col_width = 0
        demerge_cols, demerge_col_inner = [], []
        while col_index < len(standard_row):
            s_col_pos = standard_row[col_index]['pos']
            text = standard_row[col_index]['text']
            sum_col_width += s_col_pos['w']
            demerge_cols.append(s_col_pos)
            demerge_col_inner.append(text)
            # todo 先暂时使用sum_col_width > col_width
            if sum_col_width > col_width or abs(col_width - sum_col_width) < 2 or abs(
                col_width - (sum_col_width + Decimal(len(demerge_cols) / 2))) < 2:
                break
            col_index += 1
        return demerge_cols

    @staticmethod
    def delete_table_col(table_data, col_index):
        try:
            for row in table_data:
                row.pop(col_index)
        except Exception as e:
            print(e)

    @staticmethod
    def merge_table_cols(table_row):
        """
        如果同一行中单元格的right值相同，则合并为一个单元格
        @param table_row:
        @return:
        """
        n = 0
        while n < len(table_row):
            col = table_row[n]
            pos = col['pos']
            x = n + 1
            while x < len(table_row):
                c_col = table_row[x]
                c_pos = c_col['pos']
                if pos['r'] == c_pos['r']:
                    col['text'] += c_col['text']
                    table_row.pop(x)
                    continue
                x += 1
            n += 1

    def recursion(self, table_data, doc_dict, tmp_index):
        n, table_name, result_row = 0, '', []
        while n < len(table_data):
            table_row = table_data[n]
            self.merge_table_cols(table_row)
            row_val_result, row_inner = self._get_col_val(table_row)
            if row_inner and self.row_name_is_paragraph(row_inner, table_row, table_data, n, tmp_index):  # (self.check_is_title(row_inner, table_row) or self.col_is_pgh(table_row, row_inner, table_data, n)):
                pos = table_row[0]['pos']
                if len(result_row):
                    if not len(doc_dict):
                        table_name = self.get_table_name([], tmp_index)
                    else:
                        table_name = self.get_table_name(doc_dict)
                    doc_dict.append({
                        's': 'format',
                        'el_type': 'table',
                        'table_name': table_name,
                        'table_data': result_row
                    })
                table_data.pop(n)
                doc_dict.append({
                    'el_type': 'p',
                    'text': row_inner,
                    'style_dict': pos
                })
                remain_table_data = table_data[n:]
                if len(remain_table_data):
                    return self.recursion(remain_table_data, doc_dict, tmp_index)
            if self.row_have_value(table_row):
                result_row.append(table_row)
            else:
                table_data.pop(n)
                continue
            n += 1

        if len(table_data):
            if len(doc_dict):
                table_name = self.get_table_name()
                doc_dict.append({
                    'el_type': 'table',
                    's': 'append',
                    'table_name': table_name,
                    'table_data': table_data
                })
        return doc_dict

    def insert_row_col(self, s_col, row, row_index, s_col_index, _type, table_data=[], standard_row=[]):
        """
        对当前的列进行补充
        @param standard_row: 标准行
        @param table_data: 表格数据
        @param _type: 拆分还是插入
        @param s_col: 标准行的当前行
        @param row: 当前行
        @param row_index: 当前行的索引
        @param s_col_index: 标准行当前列的索引
        @return:
        """
        n = row_index - 1
        table_data = table_data if table_data else self.rows
        while n > -1:
            def recursion(num):
                if num > -1:
                    cols = table_data[num]
                    for col in cols:
                        #  针对普通股股本结构这样的有合并表头的表
                        col_rect = self.target_col_rect(table_data, len(standard_row), 'w', s_col_index)
                        if s_col['pos']['x'] == col['pos']['x'] and col['pos']['w'] not in col_rect:
                            split_cols = self.demerge_col(col['pos']['w'], standard_row, s_col_index)
                            text = col['text']
                            for index, sp in enumerate(split_cols):
                                create_col = {
                                    'pos': sp,
                                    'text': text
                                }
                                row.insert(index, create_col)
                            return True

                        if col['pos']['w'] in col_rect and col['pos']['x'] == s_col['pos']['x']:
                            if _type == 'insert':
                                row.insert(s_col_index, col)
                                return True

                            if _type == 'append':
                                row.append(col)
                                return True
                    num -= 1
                    return recursion(num)

            if recursion(n):
                break
            n -= 1

            # for col in cols:
            #     #  针对普通股股本结构这样的有合并表头的表
            #     if s_col['pos']['x'] == col['pos']['x'] and col['pos']['w'] > s_col['pos']['w']:
            #         split_cols = self.demerge_col(col['pos']['w'], standard_row, s_col_index)
            #         text = col['text']
            #         for index, sp in enumerate(split_cols):
            #             create_col = {
            #                 'pos': sp,
            #                 'text': text
            #             }
            #             row.insert(index, create_col)
            #         if_break = True
            #         break
            #
            #     if col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x']:
            #         if _type == 'insert':
            #             row.insert(s_col_index, col)
            #             if_break = True
            #             break
            #
            #         if _type == 'append':
            #             if_break = True
            #             row.append(col)
            #             break
            #
            #
            # if if_break:
            #     break
            # n -= 1

    def set_col_pos_text(self, row, col_pos, standard_row, index, col):
        """
        拆分单元格
        @param row: 当前行
        @param col_pos: 当前列的pos
        @param standard_row: 标准行，需要在里面确定当前列要拆分成几个单元格
        @param index: 标准行的索引
        @param col: 当前行的列，需要里面的内容来对拆分的单元格进行内容的补充
        @return:
        """
        # if re.search('表$', col['text']):
        #     pass
        split_cols = self.demerge_col(col_pos['w'], standard_row, index)
        text = col['text']
        for m_index, pos_col in enumerate(split_cols):
            create_col = {
                'pos': pos_col,
                'text': text
            }
            row.insert(index + m_index, create_col)
        row.pop(len(split_cols) + index)

    def merge_table_row(self, table_data):
        self.delete_surplus_first_col(table_data)
        row_lens_arr = self.get_max_row_len(table_data)
        if len(list(set(row_lens_arr))) > 1:
            max_len = max(row_lens_arr)
            index = row_lens_arr.index(max_len)
            standard_row = table_data[index]  # 拿一个标准行出来做参照使用
            ''' 分为两组，如果当前行的列少于max_len，则从当前行往上找  '''
            ''' 拿当前行的首列和上一行的首列比较，若是上一行的首列的left值小于当前首列的left值， '''
            n = len(table_data) - 1
            while n > -1:
                row = table_data[n]
                if len(row) == max_len:
                    n -= 1
                    continue
                self.process_table_cols(standard_row, row, n, table_data)
                n -= 1

    @staticmethod
    def get_first_col_left(table_data, row_index):
        result = set()
        for index, item in enumerate(table_data):
            if not len(item) or index == row_index:
                continue
            result.add(item[0]['pos']['x'])
        return result

    @staticmethod
    def get_first_col_vals(table_data):
        vals = set()
        for row in table_data:
            first_col = row[0]
            vals.add(bool(first_col['text']))
        return vals

    def delete_surplus_first_col(self, table_data):
        """
        删除首列多余的列，避免在拆分以及合并单元格时出现问题，P102=>2018 年 12 月 31 日单项金额重大并单独计提坏账准备的应收账款：
        根据首列的left值来判断删除
        @param table_data:
        @return:
        """
        first_col_vals = self.get_first_col_vals(table_data)
        for index, row in enumerate(table_data):
            cols_left = self.get_first_col_left(table_data, index)
            first_col = row[0]
            if len(first_col_vals) == 1 and list(first_col_vals)[0] is False:  # 如果第一列都是空值，也删除
                row.pop(0)
                continue

            if not first_col['text']:
                if first_col['pos']['x'] not in cols_left:
                    row.pop(0)

    def process_table_cols(self, standard_row, row, row_index, table_data=[]):
        """
        @param table_data: 表格数据
        @param standard_row: 标准行
        @param row: 当前行
        @param row_index: 行前行索引
        @return:
        """
        for s_index, s_row in enumerate(standard_row):
            if s_index > len(row) - 1:
                self.insert_row_col(s_row, row, row_index, s_index, 'append', table_data, standard_row)
                continue

            if self.check_col_pos(s_row, row[s_index]):
                continue

            if not self.check_col_pos(s_row, row[s_index]):
                ''' 如果当前行的x的列的x值大于标准行对应列的x值，则应该在当前行的列之前补充一列 '''
                pos, s_pos = row[s_index]['pos'], s_row['pos']

                if s_pos['x'] < pos['x']:
                    self.insert_row_col(s_row, row, row_index, s_index, 'insert', table_data, standard_row)

                # if s_pos['x'] == pos['x'] and pos['w'] > s_pos['w']:
                # 如果标准行的列的left值和当前列的left值相等，但是当前列的列宽大于标准列的列宽，则要拆分当前列。
                if s_pos['x'] == pos['x']:
                    col_rect_w = self.target_col_rect(table_data, len(standard_row), 'w', s_index)
                    if pos['w'] not in col_rect_w:
                        self.set_col_pos_text(row, pos, standard_row, s_index, row[s_index])

    @staticmethod
    def target_col_rect(table_data, col_len, attr, col_index):
        """
        获取所有标准行的attr属性（attr：x、w、h）
        @param col_index: 标准行对应的列
        @param table_data: 数据源
        @param col_len: 标准行的长度
        @param attr: 属性
        @return:
        """
        col_attrs = set()
        for row in table_data:
            if len(row) == col_len:
                col_attrs.add(row[col_index]['pos'][attr])
        return col_attrs

    def merge_and_clear_table(self, table_data, index):
        self.merge_table_row(table_data)
        self.clear_empty_row(table_data, index)

    def process_table_params(self, res_data):
        for index, data in enumerate(res_data):
            if data['el_type'] == 'table':
                self.merge_and_clear_table(data['table_data'], index)
        return res_data

    @staticmethod
    def get_table_current_row_val(table_data, col_index=0):
        for index, row in table_data:
            if row[col_index]['text']:
                return True
        return False

    def clear_empty_row(self, table_data, index):
        """ 对表格中的空列进行处理 """
        if not len(table_data):
            return False
        cols_val = []
        col_len = len(table_data[0])
        col_val = ''
        for col in range(col_len):
            col_list = []
            for row in table_data:
                try:
                    _bool = bool(row[col]['text'] == col_val)
                    if col_len - 1 > col > 0:
                        if row[col + 1]['text'] == row[col]['text'] or row[col - 1]['text'] == row[col]['text']:  # 强迫被拆分的列
                            _bool = True
                    col_list.append(_bool)
                    col_val = row[col]['text']
                except Exception as e:
                    print(e)
            cols_val.append(col_list)
            col_val = ''
        n = 0

        prev_table = []
        if len(self.doc_dict) > index:
            prev_doc_dict = self.doc_dict[index - 1]
            if prev_doc_dict['el_type'] == 'table':
                prev_table = prev_doc_dict['table_data']

        while n < len(cols_val):
            col_status = list(set(cols_val[n]))
            if len(col_status) and col_status[0]:  # 删除空列
                if prev_table:
                    if not self.get_table_current_row_val(prev_table, n):
                        self.delete_table_col(table_data, n)
                        cols_val.pop(n)
                        continue
                self.delete_table_col(table_data, n)
                cols_val.pop(n)
                continue
            n += 1

    def format_table(self, tmp_index, table_data):
        """ 将段落和表格拆分出来 """
        doc_dict = []
        doc_dict = self.recursion(table_data, doc_dict, tmp_index)
        if len(doc_dict):
            doc_dict = self.process_table_params(doc_dict)
            self.doc_dict.pop(tmp_index)
            left_doc_dict = self.doc_dict[0: tmp_index]
            right_doc_dict = self.doc_dict[tmp_index:]
            self.doc_dict = left_doc_dict + doc_dict + right_doc_dict
            self.loop_index += len(doc_dict)
            return True
        self.merge_and_clear_table(table_data, tmp_index)

    def get_table_name(self, doc_dict=[], tmp_index=None):
        doc_dict = doc_dict if doc_dict else self.doc_dict
        n = len(doc_dict) - 1
        if tmp_index:
            n = tmp_index
        table_name = ''
        while n > -1:
            temp_dict = doc_dict[n]
            if temp_dict['el_type'] == 'table':
                n -= 1
                continue
            try:
                text = temp_dict['text']
                if self.exclude_table_name(text) or text == '' or text.isdigit():
                    n -= 1
                    continue
                else:
                    table_name = re.sub('[\(|（].*(续|续上表)[\)|）]|', '', text)
                    break
            except Exception as e:
                print(e)
        return util.del_the_sequence(table_name)

    def process_element(self, _class, item, index):
        pass

    def check_end(self):
        pass

    @staticmethod
    def get_row_values(table_row):
        result = []
        for col in table_row:
            result.append(col['text'])
        return result

    def check_is_title(self, row_inner, table_row):
        is_title = self.util.check_is_title(row_inner)
        if re.search('\d{4}年\d{1,2}月.*计提.*(账款)$', row_inner):  # 先加一些规则来判断 P127
            return True
        return is_title and bool(len(table_row) < 3)


class ProcessTable(AnalyzeTable):
    def __init__(self):
        super(ProcessTable, self).__init__()
        self.loop_index = 0
        self.first_child = False

    def is_exclude_sentence(self, index, item, _class):
        if self.is_table:
            return False

        if index < 4:
            if self.save_first_child_text(item):
                return True

        if item.name == 'div' and self.first_child is False:  # 页眉不读
            self.first_child = True
            return True

        if self.exclude_elem(item, index, _class):
            return True

        return False

    def process_element(self, _class, elem, index):
        """
       @msg: 解析元素
       @param _class：当前元素的class，
       @param 段落的class一般为[m0 x3 h21 y148 ff2 fs2 fc0 sc1 ls0 ws0]，其中h21中的h表示元素的高度，后面的数字越大则元素的高度越高
       @param 单元格的class一般为[x21 y140 w24 h42]
       @param elem：当前元素
       """

        if self.is_exclude_sentence(index, elem, _class):
            return False

        class_name, elem_type = self.get_elem_type(_class)
        if class_name and elem_type:
            text = re.sub(' ', '', elem.text)
            style_dict = self.get_elem_style(_class)

            if re.search(self.EXCLUDE_TABLE_NAME, text):  # todo 这里有bug，不能直接判断
                elem_type = 'p'

            # 存之前判断是否是同一段落的
            if elem_type == 'p':
                return self.save_pgh(elem_type, text, style_dict)

            if elem_type == 'table':
                if self.exclude_table_val(_class):
                    return self.save_table(style_dict, text)

    def merge_table_data(self):
        self.table_name = self.get_table_name()
        if len(self.row):
            self.rows.append(self.row)
            self.row = []
        self.doc_dict.append({
            'el_type': 'table',
            'table_name': self.table_name,
            'table_data': self.rows
        })
        self.table_name = '', []
        if not len(self.doc_dict):
            return False
        last_child = self.doc_dict[-1]
        # try:
        #     if last_child['el_type'] == 'table':
        #         if (last_child['table_name'] == '' and self.table_name == '') or (
        #             last_child['table_name'] == self.table_name):
        #             last_child['table_data'] += self.rows
        #             self.rows = []
        #     else:
        #         self.table_name = self.get_table_name()
        #         self.doc_dict.append({
        #             'el_type': 'table',
        #             'table_name': self.table_name,
        #             'table_data': self.rows
        #         })
        #         self.table_name = '', []
        # except Exception as e:
        #     print(e)

    @staticmethod
    def if_merge(fs, x, h, y, prev_dict, style_dict, text):
        if fs == style_dict['fs'] and (style_dict['x'] <= x or style_dict['y'] - y <= 2):
            # and (h == style_dict['h'] or abs(y - style_dict['y'] <= 5))
            if not re.search('(\.|。)$', prev_dict['text']):
                return True

    @staticmethod
    def sentence_end_is_date(prev_dict, text):
        if re.search('[年月]$', prev_dict['text']) and re.search('^\d{1,2}', text):
            return True

        if re.search('\d{1,4}$', prev_dict['text']) and re.search('^[年月日]', text):
            return True

        return False

    def merge_elem_sentence(self, style_dict, text):
        if len(self.doc_dict):
            try:
                prev_dict = self.doc_dict[-1]
                info = self.util.get_style_info(text)

                if prev_dict['el_type'] == 'table':
                    return False

                prev_style_dict = prev_dict['style_dict']
                fs, x, h, y, prev_text = prev_style_dict['fs'], prev_style_dict['x'], prev_style_dict['h'], prev_style_dict['y'], prev_dict['text']

                if info:
                    if not self.sentence_end_is_date(prev_dict, text):
                        return False

                if re.search('[:：]$|(不?适用)$', prev_text):
                    return False

                if re.search('^[√□]|适用□?.*不适用|^(单位).*[:：]?.*元?', text):
                    return False

                if self.if_merge(fs, x, h, y, prev_dict, style_dict, text):
                    prev_dict['text'] += text
                    prev_dict['style_dict'] = style_dict
                    return True

                if info:  # todo 14日至长期，注册资本200万元。 14会被当成title的序号
                    return False

                if re.search('.*表$', text):
                    return False

                if prev_dict['el_type'] == 'table':
                    return False

                if not prev_style_dict:
                    return False
            except Exception as e:
                print(e)
        return False

    def sentence_is_table_name(self, text):
        """ 当前段落如果是 续上表、xx表（续）这种的就不保存了 """
        text = re.sub('[\(|（].*(续|续上表)[\)|）]|', '', text)
        if len(self.doc_dict):
            last_doc_dict = self.doc_dict[-1]
            if not text:
                return True
            if last_doc_dict['el_type'] == 'table':
                if last_doc_dict['table_name'] == text:
                    return True
        return False

    def save_pgh(self, elem_type, text, style_dict):
        if self.is_table:
            self.merge_table_data()  # 对表格的一些合并处理
            self.is_table, self.rows, self.table_name = False, [], ''

        if text:
            if self.sentence_is_table_name(text):
                return False
            if not self.merge_elem_sentence(style_dict, text):
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
        while self.loop_index < len(self.doc_dict):
            tmp = self.doc_dict[self.loop_index]
            if tmp['el_type'] == 'table':
                self.format_table(self.loop_index, tmp['table_data'])
            self.loop_index += 1
        print(json.dumps(self.doc_dict, ensure_ascii=False, cls=DecimalEncoder))


if __name__ == '__main__':
    app.run(host='localhost', port='9527', debug=True)
    # process = ProcessTable()
    # process.start()
