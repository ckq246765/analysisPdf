#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from bs4 import BeautifulSoup
from decimal import Decimal


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
    def exclude_elem(elem, index):
        in_text = re.sub(' ', '', elem.text)
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
            if last_cell['pos']['y'] != current_style['y']:
                return False
        return True
        ''''
            row: [{ pos: {}, text: '科目' }]
            row: [{ pos: {}, text: '上年' }, { pos: {}, text: '同期' }]
            row: [{ pos: {}, text: '前' }, { pos: {}, text: '后' }, { pos: {}, text: '前' }, { pos: {}, text: '后' }]
        
        '''

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

                self.insert_col(standard_row, row, n)

                # self.process_cell(row, standard_row)  # 对列做合并 补全处理
                n -= 1

    def insert_col(self, standard_row, row, row_index):
        """
        @param standard_row: 标准行
        @param row: 当前行
        @param row_index: 行索引
        @return:
        """
        for index, col in enumerate(standard_row):
            s_pos = col['pos']
            pos = row[index]['pos']
            if pos['x'] > s_pos['x']:
                insert_col = self.get_insert_col(index, s_pos, row_index)
                if insert_col:
                    row.insert(index, insert_col)
                    if len(row) == len(standard_row):
                        break
                    else:
                        self.process_cell(row, standard_row, index + 1)

    def get_insert_col(self, index, s_pos, row_index):
        """
        @param index: 标准列索引
        @param s_pos: 标准列样式
        @param row_index: 行索引
        @return:
        """
        is_break = False
        insert_col = {}
        while row_index > -1:
            row = self.rows[row_index]
            for col in row:
                pos = col['pos']
                if pos['x'] == s_pos['x'] and pos['w'] == s_pos['w']:
                    insert_col = col
                    is_break = True
                    break
            if is_break:
                break
            row_index -= 1
        return insert_col

    def process_cell(self, row, standard_row, index):
        """
        @param row: 当前行
        @param standard_row: 标准当前行
        @param index: 列索引
        @return:
        """
        while index < len(standard_row):
            col = row[index]
            col_pos = col['pos']
            standard_col_pos = standard_row[index]['pos']
            if col_pos['x'] == standard_col_pos['x'] and col_pos['w'] != standard_col_pos['w']:
                ''' demerge_cols：要对当前列拆分多少次，每次的pos '''
                demerge_cols = self.demerge_col(col_pos['w'], standard_row, index)

    def demerge_col(self, col_width, standard_row, col_index):
        '''拆分列'''
        sum_col_width = 0
        demerge_cols = []
        while col_index < len(standard_row):
            s_col_pos = standard_row[col_index]['pos']
            sum_col_width += s_col_pos['w']
            demerge_cols.append(s_col_pos['w'])
            if abs(col_width - sum_col_width) < 2:
                break
            col_index += 1
        return demerge_cols





    def get_before_col(self, pos, n, s_row_pos):
        n -= 1
        while n > -1:
            row_pos = self.rows[n][0]['pos']
            if pos['y'] == row_pos['y'] and s_row_pos['w'] == row_pos['w'] and pos['x'] > row_pos['x']:
                return self.rows[n]
            n -= 1
        return {}

    def save_table_last_row(self):
        if len(self.row):  # 最后一行要在读到段落的时候保存进rows里面
            self.rows.append(self.row)
            self.merge_table_row()

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
       @msg: 解析元素
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
                if con_index == 9:
                    children = content.contents[0].contents  # 只取第一层子集
                    for index, item in enumerate(children):
                        if not self.is_table and self.exclude_elem(item, index):
                            continue
                        _class = item.attrs['class'][1:]
                        self.process_element(_class, item, index)
            self.check_end()
        print(self.doc_dict)


if __name__ == '__main__':
    process = ProcessHtml()
    process.start()
