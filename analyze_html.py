#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from bs4 import BeautifulSoup
from decimal import Decimal
from util_base.util import util


class ProcessHtml:

    def __init__(self):
        self.style_content = ''
        self.doc_dict = []
        self.row = []
        self.rows = []
        self.is_table = False
        self.table_name = ''

    def save_el_style(self, soup):
        content = []
        style = soup.find_all('style')
        for sty in style:
            content += sty.contents
        self.style_content = ''.join(content)

    @staticmethod
    def exclude_elem(elem, index, _class):
        in_text = re.sub(' ', '', elem.text)
        for cls in _class:
            if re.search('^(ls)', cls):
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
        return style_dict

    def merge_elem_sentence(self, style_dict, text):
        if len(self.doc_dict):
            prev_dict = self.doc_dict[-1]
            prev_style_dict = prev_dict['style_dict']
            if not prev_style_dict:
                return False
            fs, x, h, y = prev_style_dict['fs'], prev_style_dict['x'], prev_style_dict['h'], prev_style_dict['y']
            if (fs == style_dict['fs'] and (style_dict['x'] <= x) and not re.search('\.|。', prev_dict['text']) and h ==
                style_dict['h']) or (abs(y - style_dict['y'] <= 5)):
                prev_dict['text'] += text
                prev_dict['style_dict'] = style_dict
                return True
        return False

    @staticmethod
    def exclude_table_name(sentence):
        value_pattern = u"((?<![^\(（\s])单位(?!情况)|单位(?=:|：)|(?<!\S)单元|(?<!的|及|和|\S)(?<!单项|款项|账面)金额)|（除特别注明外，金额单位均为(?:人民币)元）"
        return bool(re.search(value_pattern, sentence))

    def get_table_name(self):
        n = len(self.doc_dict) - 1
        table_name = ''
        while n > 0:
            temp_dict = self.doc_dict[n]
            text = temp_dict['text']
            if self.exclude_table_name(text):
                n -= 1
                continue
            else:
                table_name = text
                break
        return table_name

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
    def is_row_line(current_style, rows):
        """ 是否是同一行 """
        if len(rows):
            first_row_pos = rows[0][0]['pos']  # 第0行第0列
            if first_row_pos['x'] == current_style['x']:
                return True
        return False

    def reset_params(self):
        self.row, self.rows = [], []
        self.table_name = ''

    @staticmethod
    def get_max_row_len(rows):
        row_lens_arr = []
        for index, item in enumerate(rows):
            row_lens_arr.append(len(item))
        return row_lens_arr

    def merge_table_row(self):
        row_lens_arr = self.get_max_row_len(self.rows)
        if len(list(set(row_lens_arr))) > 1:
            max_len = max(row_lens_arr)
            index = row_lens_arr.index(max_len)
            standard_row = self.rows[index]  # 拿一个标准行出来做参照使用
            ''' 分为两组，如果当前行的列少于max_len，则从当前行往上找  '''
            ''' 拿当前行的首列和上一行的首列比较，若是上一行的首列的left值小于当前首列的left值， '''
            n = len(self.rows) - 1
            while n > -1:
                row = self.rows[n]
                if len(row) == max_len:
                    n -= 1
                    continue
                self.process_table(standard_row, row, n)
                n -= 1

    @staticmethod
    def check_col_pos(col, s_col):
        return bool(col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x'])

    def insert_row_col(self, s_col, row, row_index, s_col_index, type):
        """
        对当前的列进行补充
        @param s_col: 标准行的当前行
        @param row: 当前行
        @param row_index: 当前行的索引
        @param s_col_index: 标准行当前列的索引
        @return:
        """
        n = row_index - 1
        if_break = False
        while n > -1:
            cols = self.rows[n]
            for col in cols:
                if col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x']:
                    if type == 'insert':
                        row.insert(s_col_index, col)
                        if_break = True
                        break

                    if type == 'append':
                        if_break = True
                        row.append(col)
                        break
            if if_break:
                break
            n -= 1

    def process_table(self, standard_row, row, row_index):
        """
        @param standard_row: 标准行
        @param row: 当前行
        @param row_index: 行前行索引
        @return:
        """
        # def recursion():
        #
        #
        #
        #     if len(row) != len(standard_row):
        #         pass
        #     pass
        #
        # recursion()

        for s_index, s_row in enumerate(standard_row):
            if s_index > len(row) - 1:
                self.insert_row_col(s_row, row, row_index, s_index, 'append')
                continue

            if self.check_col_pos(s_row, row[s_index]):
                continue

            if not self.check_col_pos(s_row, row[s_index]):
                ''' 如果当前行的x的列的x值大于标准行对应列的x值，则应该在当前行的列之前补充一列 '''
                pos, s_pos = row[s_index]['pos'], s_row['pos']

                if s_pos['x'] < pos['x']:
                    self.insert_row_col(s_row, row, row_index, s_index, 'insert')

                if s_pos['x'] == pos['x'] and pos['w'] > s_pos['w']:
                    self.set_col_pos_text(row, pos, standard_row, s_index, row[s_index])

    def delete_merge_col(self, current_row, row_index):
        """
        删除合并过的行或列，如果当前行的所有列在之后的行的列里面都能找到，则删除整行
        @param current_row: 当前行
        @param row_index: 当前行索引
        @return:
        """
        result_list, is_del = [], False
        for index, col in enumerate(current_row):
            c_pos = col['pos']
            while row_index < len(self.rows):
                row = self.rows[row_index]
                pos = row[index]['pos']
                result_list.append(bool(pos == c_pos))
                if len(result_list) == len(current_row) and False not in result_list:
                    is_del = True
                    break
                row_index += 1
        if is_del:
            self.rows.pop(row_index)
        return is_del

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
        if re.search('表$', col['text']):
            pass
        split_cols = self.demerge_col(col_pos['w'], standard_row, index)
        text = col['text']
        for m_index, pos_col in enumerate(split_cols):
            create_col = {
                'pos': pos_col,
                'text': text
            }
            row.insert(index + m_index, create_col)
        row.pop(len(split_cols) + index)

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
        demerge_cols = []
        while col_index < len(standard_row):
            s_col_pos = standard_row[col_index]['pos']
            sum_col_width += s_col_pos['w']
            demerge_cols.append(s_col_pos)
            if abs(col_width - sum_col_width) < 2:
                break
            col_index += 1
        return demerge_cols

    @staticmethod
    def _get_col_val(row):
        result = set()
        for col in row:
            result.add(col['text'])
        return list(result)

    def get_col_name_occurrences(self, row):
        for col in row:
            text = col['text']
            if self.get_count(row, text) > 2:
                return True
        return False

    @staticmethod
    def row_have_value(row):
        result = []
        for col in row:
            text = col['text']
            if text:
                result.append(text)
        return bool(len(result))

    def format_table_data(self):
        """
        格式化table，针对表嵌表的情况，标题表格也被存入表中，需要拆出来
        @return:
        """
        index = 0
        table_data = []
        while index < len(self.rows):
            row = self.rows[index]
            is_continue = False
            col_inner = ''.join(self._get_col_val(row))
            _join_cols_val = util.check_is_title(col_inner)
            for col in row:
                text = col['text']
                if (util.check_is_title(text) or _join_cols_val) and self.get_count(row, text) > 2:
                    if len(table_data):
                        # 在遇到新的标题前，将表格数据保存起来
                        self.save_doc_dict('', 'table', {}, False, table_data)
                        table_data = []

                    # 如果当前列中含有标题，则把整列删除，并保存为标题
                    self.rows.pop(index)
                    self.save_doc_dict(col['text'], 'p', col['pos'], True)
                    is_continue = True
                    break
            if is_continue:
                continue
            else:
                if self.row_have_value(row):  # 行数据都为空的，就排除掉
                    table_data.append(row)
            index += 1
        print(self.rows)

    def clear_empty_row(self, table_data):
        """ 对表格中的空列进行处理 """

        for row in table_data:
            pass


    def save_doc_dict(self, pgh='', dict_type='p', style_dict={}, level=False, table_data=[]):
        table_name = ''
        if dict_type == 'table':
            table_name = self.get_table_name()
            self.clear_empty_row(table_data)
        temp_dict = {
            'el_type': dict_type,
            'level': level,
            'text': pgh,
            'table_name': table_name,
            'table_data': table_data,
            'style_dict': style_dict
        }
        self.doc_dict.append(temp_dict)

    @staticmethod
    def get_count(row, col_text):
        text_result = []
        for col in row:
            text_result.append(col['text'])
        return text_result.count(col_text)

    def save_table_last_row(self):
        if len(self.row):  # 最后一行要在读到段落的时候保存进rows里面
            self.rows.append(self.row)
            self.merge_table_row()
            self.format_table_data()
            self.doc_dict.append({
                'el_type': 'table',
                'text': '',
                'table_name': self.table_name,
                'table_data': self.rows,
                'style_dict': ''
            })
            self.reset_params()

    def check_end(self):
        self.save_table_last_row()

    def process_element(self, _class, elem, index):
        """
       @param index: 页码
       @param _class：当前元素的class，
       @param 段落的class一般为[m0 x3 h21 y148 ff2 fs2 fc0 sc1 ls0 ws0]，其中h21中的h表示元素的高度，后面的数字越大则元素的高度越高
       @param 单元格的class一般为[x21 y140 w24 h42]
       @param elem：当前元素
       """
        # 判断当前元素的类型
        class_name, elem_type = self.get_elem_type(_class)
        if class_name and elem_type:
            text = re.sub(' ', '', elem.text)
            style_dict = self.get_elem_style(_class)
            # 存之前判断是否是同一段落的
            if elem_type == 'p':
                self.is_table = False
                self.save_table_last_row()
                if not text:
                    return False

                if self.merge_elem_sentence(style_dict, text):
                    return False

                self.doc_dict.append({
                    'el_type': elem_type,
                    'text': text,
                    'table_name': '',
                    'style_dict': style_dict
                })

            if elem_type == 'table':
                self.is_table = True
                # 单元可以根据bottom的值来判断是不是同一行
                if not self.table_name:
                    self.table_name = self.get_table_name()
                temp_dict = {'pos': style_dict, 'text': text}
                if self.is_same_line(style_dict, self.row) and not self.is_row_line(style_dict, self.rows):
                    self.row.append(temp_dict)
                else:
                    self.rows.append(self.row)
                    self.row = []
                    self.row.append(temp_dict)

    def start(self):
        soup = BeautifulSoup(open('test.p.html', encoding='utf-8'), features='html.parser')
        self.save_el_style(soup)
        contents = soup.find_all('div', id=re.compile('^(pf).*[\d|[a-zA-Z]'))  # 获取page
        if len(contents):
            for con_index, content in enumerate(contents):
                if con_index in [99]:
                    children = content.contents[0].contents  # 只取第一层子集
                    first_child = False
                    for index, item in enumerate(children):
                        _class = item.attrs['class'][1:]
                        if item.name == 'div' and first_child is False:  # 页眉不读
                            first_child = True
                            continue

                        if not self.is_table and self.exclude_elem(item, index, _class):
                            continue
                        self.process_element(_class, item, index)
            self.check_end()
        print(self.doc_dict)


if __name__ == '__main__':
    process = ProcessHtml()
    process.start()
