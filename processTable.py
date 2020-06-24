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

    def __init__(self):
        self.style_content = ''
        self.doc_dict = []
        self.row = []
        self.rows = []
        self.is_table = False
        self.table_name = ''
        self.page_width = ''
        self.util = util
        self.footer_values = set()
        self.exclude_list = []

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
                if self.page_width and (self.page_width - left) <= 5 and text.isdigit(): # 一般是页码数，不处理
                    return True

        if index == 1 and re.search('公告编号', in_text):
            return True
        if (index == 0 and elem.name == 'img') or elem.name == 'a':  # img标签和a标签不解析
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
                if con_index < 7:  # con_index in [7, 8, 9] con_index in [130, 131, 132, 133, 134, 135, 136]:  # con_index in [36, 37] in [103]:  # con_index in [103]
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

                        if self.exclude_elem(item, index, _class):
                            continue
                        self.process_element(_class, item)

            self.check_end()
            end = datetime.datetime.now()
            print("文档IO用时：" + str((end - start).seconds) + u"秒")
            return json.dumps(self.doc_dict, ensure_ascii=False, cls=DecimalEncoder)

    @staticmethod
    def exclude_table_name(sentence):
        value_pattern = u"((?<![^\(（\s])单位(?!情况)|单位(?=:|：)|(?<!\S)单元|(?<!的|及|和|\S)(?<!单项|款项|账面)金额)|（除特别注明外，金额单位均为(?:人民币)元）|□不适用|√"
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
            try:
                result.append(col['text'])
            except Exception as e:
                print(e)
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
        if len(row) > 1:
            for col in row:
                col_values.add(col['text'])
        return bool(len(col_values) == 1)

    @staticmethod
    def check_col_pos(col, s_col):
        return bool(col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x'])

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
    def delete_table_col(table_data, col_index):
        for row in table_data:
            row.pop(col_index)

    def recursion(self, table_data, doc_dict, tmp_index):
        n, table_name, result_row = 0, '', []
        while n < len(table_data):
            table_row = table_data[n]
            row_inner = self._get_col_val(table_row)
            if row_inner and (self.check_is_title(row_inner, table_row) or self.col_is_pgh(table_row)):
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
        if_break = False
        table_data = table_data if table_data else self.rows
        while n > -1:
            cols = table_data[n]
            for col in cols:
                #  针对普通股股本结构这样的有合并表头的表
                if s_col['pos']['x'] == col['pos']['x'] and col['pos']['w'] > s_col['pos']['w']:
                    split_cols = self.demerge_col(col['pos']['w'], standard_row, s_col_index)
                    text = col['text']
                    for index, sp in enumerate(split_cols):
                        create_col = {
                            'pos': sp,
                            'text': text
                        }
                        row.insert(index, create_col)

                if col['pos']['w'] == s_col['pos']['w'] and col['pos']['x'] == s_col['pos']['x']:
                    if _type == 'insert':
                        row.insert(s_col_index, col)
                        if_break = True
                        break

                    if _type == 'append':
                        if_break = True
                        row.append(col)
                        break
            if if_break:
                break
            n -= 1

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

    def merge_table_row(self, table_data):
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

                if s_pos['x'] == pos['x'] and pos['w'] > s_pos['w']:
                    self.set_col_pos_text(row, pos, standard_row, s_index, row[s_index])

    def merge_and_clear_table(self, table_data):
        self.merge_table_row(table_data)
        self.clear_empty_row(table_data)

    def process_table_params(self, res_data):
        for data in res_data:
            if data['el_type'] == 'table':
                self.merge_and_clear_table(data['table_data'])
        return res_data

    def clear_empty_row(self, table_data):
        """ 对表格中的空列进行处理 """
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
        while n < len(cols_val):
            col_status = list(set(cols_val[n]))
            if len(col_status) and col_status[0]:  # 删除空列
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
        self.merge_and_clear_table(table_data)
        # print(self.doc_dict)
        # n, doc_dict, result_row, table_name = 0, [], [], ''
        # while n < len(table_data):
        #     table_row = table_data[n]
        #     row_inner = self._get_col_val(table_row)
        #     print('-----------row_inner------------', row_inner)
        #     if row_inner and (self.check_is_title(row_inner, table_row) or self.col_is_pgh(table_row)):
        #         if len(result_row):
        #             pos = table_row[0]['pos']
        #             pgh_dict = {
        #                 'el_type': 'p',
        #                 'text': row_inner,
        #                 'style_dict': pos
        #             }
        #             self.doc_dict.insert(tmp_index + 1, pgh_dict)
        #             pass
        #         table_data.pop(n)
        #         remain_table_data = table_data[n:]
        #         table_data = table_data[0: n]
        #         self.doc_dict.insert(tmp_index + 2, {
        #             'el_type': 'table',
        #             'table_name': row_inner,
        #             'text': '',
        #             'style_dict': {},
        #             'table_data': remain_table_data
        #         })
        #         continue
        #
        #     if self.row_have_value(table_row):
        #         result_row.append(table_row)
        #     else:
        #         table_data.pop(n)
        #         continue
        #
        #     n += 1
        # print(self.doc_dict)

    def get_table_name(self, doc_dict=[], tmp_index=None):
        doc_dict = doc_dict if doc_dict else self.doc_dict
        n = len(doc_dict) - 1
        if tmp_index:
            n = tmp_index
        table_name = ''
        while n > 0:
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
                    table_name = text
                    break
            except Exception as e:
                print(e)
        return util.del_the_sequence(table_name)

    def process_element(self, _class, item):
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
        # row_values = self.get_row_values(table_row)
        # if is_title:
        #     style_info = self.util.get_style_info(row_inner)
        #     if style_info:
        #         index = style_info['index']
        return is_title and bool(len(table_row) < 3)


class ProcessTable(AnalyzeTable):
    def __init__(self):
        super(ProcessTable, self).__init__()
        self.loop_index = 0

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
                if self.exclude_table_val(_class):
                    self.save_table(style_dict, text)

    def merge_table_data(self):
        if not len(self.doc_dict):
            return False
        last_child = self.doc_dict[-1]
        if len(self.row):
            self.rows.append(self.row)
            self.row = []
        if last_child['el_type'] == 'table':
            if (last_child['table_name'] == '' and self.table_name == '') or (last_child['table_name'] == self.table_name):
                last_child['table_data'] += self.rows
                self.rows = []
        else:
            self.table_name = self.get_table_name()
            self.doc_dict.append({
                'el_type': 'table',
                'table_name': self.table_name,
                'table_data': self.rows
            })
            self.table_name = ''

    def merge_elem_sentence(self, style_dict, text):
        if len(self.doc_dict):
            prev_dict = self.doc_dict[-1]
            if prev_dict['el_type'] == 'table':
                return False
            prev_style_dict = prev_dict['style_dict']
            if not prev_style_dict:
                return False
            fs, x, h, y = prev_style_dict['fs'], prev_style_dict['x'], prev_style_dict['h'], prev_style_dict['y']
            if (fs == style_dict['fs'] and (style_dict['x'] <= x) and not re.search('\.|。', prev_dict['text'])) and (h == style_dict['h'] or abs(y - style_dict['y'] <= 5)):
                prev_dict['text'] += text
                prev_dict['style_dict'] = style_dict
                return True
        return False

    def save_pgh(self, elem_type, text, style_dict):
        if self.is_table:
            self.merge_table_data()  # 对表格的一些合并处理
            self.is_table, self.rows, self.table_name = False, [], ''

        if text:
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
