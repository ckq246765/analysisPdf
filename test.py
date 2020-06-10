#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json

# obj = {'el_type': 'table', 'text': '', 'table_name': '√会计政策变更□会计差错更正□其他原因□不适用', 'table_data':
#     [
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('210.510000'), 'h': Decimal('31.670000')}, 'text': '科目'}],
#
#         [{'pos': {'x': Decimal('154.590000'), 'y': Decimal('226.590000'), 'h': Decimal('15.590000')},
#           'text': '上年期末（上年同期）'},
#          {'pos': {'x': Decimal('350.600000'), 'y': Decimal('226.590000'), 'h': Decimal('15.590000')},
#           'text': '上上年期末（上上年同期）'}],
#         [{'pos': {'x': Decimal('154.590000'), 'y': Decimal('210.510000'), 'h': Decimal('15.590000')}, 'text': '调整重述前'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('210.510000'), 'h': Decimal('15.590000')}, 'text': '调整重述后'},
#          {'pos': {'x': Decimal('350.600000'), 'y': Decimal('210.510000'), 'h': Decimal('15.590000')}, 'text': '调整重述前'},
#          {'pos': {'x': Decimal('448.660000'), 'y': Decimal('210.510000'), 'h': Decimal('15.590000')}, 'text': '调整重述后'}],
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('194.430000'), 'h': Decimal('15.590000')}, 'text': '应收账款'},
#          {'pos': {'x': Decimal('154.590000'), 'y': Decimal('194.430000'), 'h': Decimal('15.590000')},
#           'text': '41,687,617.55'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('194.430000'), 'h': Decimal('15.590000')},
#           'text': '41,790,706.80'}],
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('178.230000'), 'h': Decimal('15.590000')}, 'text': '其他应收款'},
#          {'pos': {'x': Decimal('154.590000'), 'y': Decimal('178.230000'), 'h': Decimal('15.590000')},
#           'text': '13,986,353.82'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('178.230000'), 'h': Decimal('15.590000')},
#           'text': '13,388,481.42'}],
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('162.150000'), 'h': Decimal('15.590000')}, 'text': '递延所得税资产'},
#          {'pos': {'x': Decimal('154.590000'), 'y': Decimal('162.150000'), 'h': Decimal('15.590000')},
#           'text': '2,842,283.98'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('162.150000'), 'h': Decimal('15.590000')},
#           'text': '2,905,216.36'}],
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('146.070000'), 'h': Decimal('15.590000')}, 'text': '未分配利润'},
#          {'pos': {'x': Decimal('154.590000'), 'y': Decimal('146.070000'), 'h': Decimal('15.590000')},
#           'text': '-6,524,503.69'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('146.070000'), 'h': Decimal('15.590000')},
#           'text': '-6,996,919.04'}],
#         [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('129.990000'), 'h': Decimal('15.590000')}, 'text': '少数股东权益'},
#          {'pos': {'x': Decimal('154.590000'), 'y': Decimal('129.990000'), 'h': Decimal('15.590000')},
#           'text': '5,911,740.26'},
#          {'pos': {'x': Decimal('252.650000'), 'y': Decimal('129.990000'), 'h': Decimal('15.590000')},
#           'text': '5,952,304.84'}]], 'style_dict': ''}

arr = [1,1,1,1,1,1]

print(max(arr))