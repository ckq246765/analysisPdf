#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from decimal import Decimal

arr = [
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('736.060000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('13.550000')}, 'text': ''}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('736.060000'), 'w': Decimal('128.420000'),
                 'r': Decimal('324.190000'), 'h': Decimal('13.550000')}, 'text': '账面余额'}, {
         'pos': {'x': Decimal('323.840000'), 'y': Decimal('736.060000'), 'w': Decimal('134.650000'),
                 'r': Decimal('458.490000'), 'h': Decimal('13.550000')}, 'text': '坏账准备'}, {
         'pos': {'x': Decimal('458.740000'), 'y': Decimal('720.940000'), 'w': Decimal('77.870000'),
                 'r': Decimal('536.610000'), 'h': Decimal('28.670000')}, 'text': '账面价值'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('720.940000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('13.550000')}, 'text': ''}, {'pos': {'x': Decimal('195.770000'), 'y': Decimal('720.940000'),
                                                          'w': Decimal('71.640000'), 'r': Decimal('267.410000'),
                                                          'h': Decimal('13.550000')}, 'text': '金额'}, {'pos': {
        'x': Decimal('267.410000'), 'y': Decimal('720.940000'), 'w': Decimal('56.784000'), 'r': Decimal('324.194000'),
        'h': Decimal('13.550000')}, 'text': '比例（%）'}, {'pos': {'x': Decimal('323.840000'), 'y': Decimal('720.940000'),
                                                               'w': Decimal('77.870000'), 'r': Decimal('401.710000'),
                                                               'h': Decimal('13.550000')}, 'text': '金额'}, {'pos': {
        'x': Decimal('401.600000'), 'y': Decimal('720.940000'), 'w': Decimal('56.654000'), 'r': Decimal('458.254000'),
        'h': Decimal('13.550000')}, 'text': '比例（%）'}], [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('706.780000'),
                                                                 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
                                                                 'h': Decimal('13.670000')}, 'text': ''}, {
                                                            'pos': {'x': Decimal('89.544000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('105.733000'),
                                                                    'r': Decimal('195.277000'),
                                                                    'h': Decimal('13.670000')}, 'text': '按单项计提坏账准'}, {
                                                            'pos': {'x': Decimal('195.770000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('71.640000'),
                                                                    'r': Decimal('267.410000'),
                                                                    'h': Decimal('13.670000')}, 'text': '4,234,699.63'},
                                                        {
                                                            'pos': {'x': Decimal('267.410000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('56.784000'),
                                                                    'r': Decimal('324.194000'),
                                                                    'h': Decimal('13.670000')}, 'text': '97.64'}, {
                                                            'pos': {'x': Decimal('323.840000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('77.870000'),
                                                                    'r': Decimal('401.710000'),
                                                                    'h': Decimal('13.670000')}, 'text': '4,134,699.63'},
                                                        {
                                                            'pos': {'x': Decimal('401.600000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('56.654000'),
                                                                    'r': Decimal('458.254000'),
                                                                    'h': Decimal('13.670000')}, 'text': '97.64'}, {
                                                            'pos': {'x': Decimal('458.740000'),
                                                                    'y': Decimal('706.780000'),
                                                                    'w': Decimal('77.870000'),
                                                                    'r': Decimal('536.610000'),
                                                                    'h': Decimal('13.670000')}, 'text': '100,000.00'}],
    [{
        'pos': {
            'x': Decimal(
                '53.750000'),
            'y': Decimal(
                '693.220000'),
            'w': Decimal(
                '35.303000'),
            'r': Decimal(
                '89.053000'),
            'h': Decimal(
                '13.550000')},
        'text': ''},
        {
            'pos': {
                'x': Decimal(
                    '89.544000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '105.733000'),
                'r': Decimal(
                    '195.277000'),
                'h': Decimal(
                    '13.550000')},
            'text': '按组合计提坏账准备'},
        {
            'pos': {
                'x': Decimal(
                    '195.770000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '71.640000'),
                'r': Decimal(
                    '267.410000'),
                'h': Decimal(
                    '13.550000')},
            'text': '102,497.83'},
        {
            'pos': {
                'x': Decimal(
                    '267.410000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '56.784000'),
                'r': Decimal(
                    '324.194000'),
                'h': Decimal(
                    '13.550000')},
            'text': '2.36'},
        {
            'pos': {
                'x': Decimal(
                    '323.840000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '401.710000'),
                'h': Decimal(
                    '13.550000')},
            'text': '9,060.00'},
        {
            'pos': {
                'x': Decimal(
                    '401.600000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '56.654000'),
                'r': Decimal(
                    '458.254000'),
                'h': Decimal(
                    '13.550000')},
            'text': '8.84'},
        {
            'pos': {
                'x': Decimal(
                    '458.740000'),
                'y': Decimal(
                    '693.220000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '13.550000')},
            'text': '93,437.83'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('679.540000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('679.540000'), 'w': Decimal('105.733000'),
                 'r': Decimal('195.277000'), 'h': Decimal('13.670000')}, 'text': '其中：'}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('679.540000'), 'w': Decimal('71.640000'),
                 'r': Decimal('267.410000'), 'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('267.410000'), 'y': Decimal('679.540000'), 'w': Decimal('56.784000'),
                 'r': Decimal('324.194000'), 'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('323.840000'), 'y': Decimal('679.540000'), 'w': Decimal('77.870000'),
                 'r': Decimal('401.710000'), 'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('401.600000'), 'y': Decimal('679.540000'), 'w': Decimal('56.654000'),
                 'r': Decimal('458.254000'), 'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('458.740000'), 'y': Decimal('679.540000'), 'w': Decimal('77.870000'),
                 'r': Decimal('536.610000'), 'h': Decimal('13.670000')}, 'text': ''}],
    [{'pos': {'x': Decimal('53.750000'),
              'y': Decimal(
                  '652.300000'),
              'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal(
                  '27.230000')},
      'text': ''}, {'pos': {
        'x': Decimal('89.544000'), 'y': Decimal('652.300000'), 'w': Decimal('105.733000'),
        'r': Decimal('195.277000'),
        'h': Decimal('27.230000')}, 'text': '组合1：合并范围内关联方款项'}, {'pos': {'x': Decimal('195.770000'),
                                                                        'y': Decimal('652.300000'),
                                                                        'w': Decimal('71.640000'),
                                                                        'r': Decimal('267.410000'),
                                                                        'h': Decimal('27.230000')}, 'text': '-'},
     {'pos': {
         'x': Decimal('267.410000'), 'y': Decimal('652.300000'), 'w': Decimal('56.784000'),
         'r': Decimal('324.194000'),
         'h': Decimal('27.230000')}, 'text': '-'}, {'pos': {'x': Decimal('323.840000'), 'y': Decimal('652.300000'),
                                                            'w': Decimal('77.870000'), 'r': Decimal('401.710000'),
                                                            'h': Decimal('27.230000')}, 'text': '-'}, {'pos': {
        'x': Decimal('401.600000'), 'y': Decimal('652.300000'), 'w': Decimal('56.654000'),
        'r': Decimal('458.254000'),
        'h': Decimal('27.230000')}, 'text': '-'}, {'pos': {'x': Decimal('458.740000'), 'y': Decimal('652.300000'),
                                                           'w': Decimal('77.870000'), 'r': Decimal('536.610000'),
                                                           'h': Decimal('27.230000')}, 'text': '-'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('625.060000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('27.230000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('625.060000'),
                                                          'w': Decimal('105.733000'), 'r': Decimal('195.277000'),
                                                          'h': Decimal('27.230000')}, 'text': '组合2：备用金、房租押金、代缴社保款'}, {
        'pos': {
            'x': Decimal(
                '195.770000'),
            'y': Decimal(
                '625.060000'),
            'w': Decimal(
                '71.640000'),
            'r': Decimal(
                '267.410000'),
            'h': Decimal(
                '27.230000')},
        'text': '72,377.83'},
        {'pos': {
            'x': Decimal(
                '267.410000'),
            'y': Decimal(
                '625.060000'),
            'w': Decimal(
                '56.784000'),
            'r': Decimal(
                '324.194000'),
            'h': Decimal(
                '27.230000')},
            'text': '1.67'}, {
            'pos': {
                'x': Decimal(
                    '323.840000'),
                'y': Decimal(
                    '625.060000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '401.710000'),
                'h': Decimal(
                    '27.230000')},
            'text': '-'}, {
            'pos': {
                'x': Decimal(
                    '401.600000'),
                'y': Decimal(
                    '625.060000'),
                'w': Decimal(
                    '56.654000'),
                'r': Decimal(
                    '458.254000'),
                'h': Decimal(
                    '27.230000')},
            'text': '-'}, {
            'pos': {
                'x': Decimal(
                    '458.740000'),
                'y': Decimal(
                    '625.060000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '27.230000')},
            'text': '72,377.83'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('611.500000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('13.550000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('611.500000'), 'w': Decimal('105.733000'),
                 'r': Decimal('195.277000'), 'h': Decimal('13.550000')}, 'text': '组合3：其他款项'}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('611.500000'), 'w': Decimal('71.640000'),
                 'r': Decimal('267.410000'), 'h': Decimal('13.550000')}, 'text': '30,120.00'}, {
         'pos': {'x': Decimal('267.410000'), 'y': Decimal('611.500000'), 'w': Decimal('56.784000'),
                 'r': Decimal('324.194000'), 'h': Decimal('13.550000')}, 'text': '0.69'}, {
         'pos': {'x': Decimal('323.840000'), 'y': Decimal('611.500000'), 'w': Decimal('77.870000'),
                 'r': Decimal('401.710000'), 'h': Decimal('13.550000')}, 'text': '9,060.00'}, {
         'pos': {'x': Decimal('401.600000'), 'y': Decimal('611.500000'), 'w': Decimal('56.654000'),
                 'r': Decimal('458.254000'), 'h': Decimal('13.550000')}, 'text': '30.08'}, {
         'pos': {'x': Decimal('458.740000'), 'y': Decimal('611.500000'), 'w': Decimal('77.870000'),
                 'r': Decimal('536.610000'), 'h': Decimal('13.550000')}, 'text': '21,060.00'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('597.340000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('13.670000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('597.340000'),
                                                          'w': Decimal('105.733000'), 'r': Decimal('195.277000'),
                                                          'h': Decimal('13.670000')}, 'text': '合计'}, {'pos': {
        'x': Decimal('195.770000'), 'y': Decimal('597.340000'), 'w': Decimal('71.640000'), 'r': Decimal('267.410000'),
        'h': Decimal('13.670000')}, 'text': '4,337,197.46'}, {'pos': {'x': Decimal('267.410000'),
                                                                      'y': Decimal('597.340000'),
                                                                      'w': Decimal('56.784000'),
                                                                      'r': Decimal('324.194000'),
                                                                      'h': Decimal('13.670000')}, 'text': '100.00'}, {
        'pos': {'x': Decimal(
            '323.840000'),
            'y': Decimal(
                '597.340000'),
            'w': Decimal(
                '77.870000'),
            'r': Decimal(
                '401.710000'),
            'h': Decimal(
                '13.670000')},
        'text': '4,143,759.63'},
        {'pos': {'x': Decimal(
            '401.600000'),
            'y': Decimal(
                '597.340000'),
            'w': Decimal(
                '56.654000'),
            'r': Decimal(
                '458.254000'),
            'h': Decimal(
                '13.670000')},
            'text': '95.54'}, {
            'pos': {'x': Decimal(
                '458.740000'),
                'y': Decimal(
                    '597.340000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '13.670000')},
            'text': '193,437.83'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('583.870000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('12.000000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('583.870000'), 'w': Decimal('489.450000'),
                 'r': Decimal('578.994000'), 'h': Decimal('12.000000')}, 'text': ''}],
    [{'pos': {'x': Decimal('53.750000'),
              'y': Decimal(
                  '571.870000'),
              'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal(
                  '12.000000')},
      'text': ''}, {'pos': {
        'x': Decimal('89.544000'), 'y': Decimal('571.870000'), 'w': Decimal('489.450000'),
        'r': Decimal('578.994000'),
        'h': Decimal('12.000000')}, 'text': ''}], [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('558.190000'),
                                                            'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
                                                            'h': Decimal('13.680000')}, 'text': ''}, {
                                                       'pos': {'x': Decimal('89.544000'), 'y': Decimal('527.950000'),
                                                               'w': Decimal('106.333000'),
                                                               'r': Decimal('195.877000'),
                                                               'h': Decimal('43.920000')}, 'text': '类别'}, {
                                                       'pos': {'x': Decimal('195.770000'),
                                                               'y': Decimal('558.190000'),
                                                               'w': Decimal('340.360000'),
                                                               'r': Decimal('536.130000'),
                                                               'h': Decimal('13.680000')}, 'text': '2018年12月31日'}],
    [{
        'pos': {
            'x': Decimal(
                '53.750000'),
            'y': Decimal(
                '543.070000'),
            'w': Decimal(
                '35.303000'),
            'r': Decimal(
                '89.053000'),
            'h': Decimal(
                '13.680000')},
        'text': ''},
        {
            'pos': {
                'x': Decimal(
                    '195.770000'),
                'y': Decimal(
                    '543.070000'),
                'w': Decimal(
                    '134.900000'),
                'r': Decimal(
                    '330.670000'),
                'h': Decimal(
                    '13.680000')},
            'text': '账面余额'},
        {
            'pos': {
                'x': Decimal(
                    '329.960000'),
                'y': Decimal(
                    '543.070000'),
                'w': Decimal(
                    '127.570000'),
                'r': Decimal(
                    '457.530000'),
                'h': Decimal(
                    '13.680000')},
            'text': '坏账准备'},
        {
            'pos': {
                'x': Decimal(
                    '458.740000'),
                'y': Decimal(
                    '527.950000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '28.800000')},
            'text': '账面价值'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('527.950000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('13.680000')}, 'text': ''}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('527.950000'), 'w': Decimal('78.240000'),
                 'r': Decimal('274.010000'), 'h': Decimal('13.680000')}, 'text': '金额'}, {
         'pos': {'x': Decimal('273.530000'), 'y': Decimal('527.950000'), 'w': Decimal('56.664000'),
                 'r': Decimal('330.194000'), 'h': Decimal('13.680000')}, 'text': '比例（%）'}, {
         'pos': {'x': Decimal('329.960000'), 'y': Decimal('527.950000'), 'w': Decimal('70.910000'),
                 'r': Decimal('400.870000'), 'h': Decimal('13.680000')}, 'text': '金额'}, {
         'pos': {'x': Decimal('401.600000'), 'y': Decimal('527.950000'), 'w': Decimal('56.654000'),
                 'r': Decimal('458.254000'), 'h': Decimal('13.680000')}, 'text': '比例（%）'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('486.670000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('40.800000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('486.670000'),
                                                          'w': Decimal('106.333000'), 'r': Decimal('195.877000'),
                                                          'h': Decimal('40.800000')}, 'text': '单项金额重大并单独计提坏账准备的应收账款'}, {
        'pos': {'x': Decimal(
            '195.770000'),
            'y': Decimal(
                '486.670000'),
            'w': Decimal(
                '78.240000'),
            'r': Decimal(
                '274.010000'),
            'h': Decimal(
                '40.800000')},
        'text': '13,860,014.22'},
        {'pos': {'x': Decimal(
            '273.530000'),
            'y': Decimal(
                '486.670000'),
            'w': Decimal(
                '56.664000'),
            'r': Decimal(
                '330.194000'),
            'h': Decimal(
                '40.800000')},
            'text': '83.83'}, {'pos': {
            'x': Decimal('329.960000'), 'y': Decimal('486.670000'), 'w': Decimal('70.910000'),
            'r': Decimal('400.870000'),
            'h': Decimal('40.800000')}, 'text': '1,090,000.00'}, {'pos': {'x': Decimal('401.600000'),
                                                                          'y': Decimal('486.670000'),
                                                                          'w': Decimal('56.654000'),
                                                                          'r': Decimal('458.254000'),
                                                                          'h': Decimal('40.800000')}, 'text': '7.86'}, {
            'pos': {'x': Decimal(
                '458.740000'),
                'y': Decimal(
                    '486.670000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '40.800000')},
            'text': '12,770,014.22'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('445.750000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('40.920000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('445.750000'), 'w': Decimal('106.333000'),
                 'r': Decimal('195.877000'), 'h': Decimal('40.920000')}, 'text': '按信用风险特征组合计提坏账准备的应收账款'}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('445.750000'), 'w': Decimal('78.240000'),
                 'r': Decimal('274.010000'), 'h': Decimal('40.920000')}, 'text': '614,638.24'}, {
         'pos': {'x': Decimal('273.530000'), 'y': Decimal('445.750000'), 'w': Decimal('56.664000'),
                 'r': Decimal('330.194000'), 'h': Decimal('40.920000')}, 'text': '3.72'}, {
         'pos': {'x': Decimal('329.960000'), 'y': Decimal('445.750000'), 'w': Decimal('70.910000'),
                 'r': Decimal('400.870000'), 'h': Decimal('40.920000')}, 'text': '96,038.04'}, {
         'pos': {'x': Decimal('401.600000'), 'y': Decimal('445.750000'), 'w': Decimal('56.654000'),
                 'r': Decimal('458.254000'), 'h': Decimal('40.920000')}, 'text': '15.63'}, {
         'pos': {'x': Decimal('458.740000'), 'y': Decimal('445.750000'), 'w': Decimal('77.870000'),
                 'r': Decimal('536.610000'), 'h': Decimal('40.920000')}, 'text': '518,600.20'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('404.930000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('40.820000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('404.930000'),
                                                          'w': Decimal('106.333000'), 'r': Decimal('195.877000'),
                                                          'h': Decimal('40.820000')}, 'text': '单项金额不重大但单独计提坏账准备的应收账款'},
        {
            'pos': {'x': Decimal(
                '195.770000'),
                'y': Decimal(
                    '404.930000'),
                'w': Decimal(
                    '78.240000'),
                'r': Decimal(
                    '274.010000'),
                'h': Decimal(
                    '40.820000')},
            'text': '2,058,713.55'},
        {'pos': {'x': Decimal(
            '273.530000'),
            'y': Decimal(
                '404.930000'),
            'w': Decimal(
                '56.664000'),
            'r': Decimal(
                '330.194000'),
            'h': Decimal(
                '40.820000')},
            'text': '12.45'}, {
            'pos': {'x': Decimal(
                '329.960000'),
                'y': Decimal(
                    '404.930000'),
                'w': Decimal(
                    '70.910000'),
                'r': Decimal(
                    '400.870000'),
                'h': Decimal(
                    '40.820000')},
            'text': '1,360,974.15'},
        {'pos': {'x': Decimal(
            '401.600000'),
            'y': Decimal(
                '404.930000'),
            'w': Decimal(
                '56.654000'),
            'r': Decimal(
                '458.254000'),
            'h': Decimal(
                '40.820000')},
            'text': '66.11'}, {
            'pos': {'x': Decimal(
                '458.740000'),
                'y': Decimal(
                    '404.930000'),
                'w': Decimal(
                    '77.870000'),
                'r': Decimal(
                    '536.610000'),
                'h': Decimal(
                    '40.820000')},
            'text': '697,739.40'}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('390.770000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('13.670000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('390.770000'), 'w': Decimal('106.333000'),
                 'r': Decimal('195.877000'), 'h': Decimal('13.670000')}, 'text': '合计'}, {
         'pos': {'x': Decimal('195.770000'), 'y': Decimal('390.770000'), 'w': Decimal('78.240000'),
                 'r': Decimal('274.010000'), 'h': Decimal('13.670000')}, 'text': '16,533,366.01'}, {
         'pos': {'x': Decimal('273.530000'), 'y': Decimal('390.770000'), 'w': Decimal('56.664000'),
                 'r': Decimal('330.194000'), 'h': Decimal('13.670000')}, 'text': '100.00'}, {
         'pos': {'x': Decimal('329.960000'), 'y': Decimal('390.770000'), 'w': Decimal('70.910000'),
                 'r': Decimal('400.870000'), 'h': Decimal('13.670000')}, 'text': '2,547,012.19'}, {
         'pos': {'x': Decimal('401.600000'), 'y': Decimal('390.770000'), 'w': Decimal('56.654000'),
                 'r': Decimal('458.254000'), 'h': Decimal('13.670000')}, 'text': '15.41'}, {
         'pos': {'x': Decimal('458.740000'), 'y': Decimal('390.770000'), 'w': Decimal('77.870000'),
                 'r': Decimal('536.610000'), 'h': Decimal('13.670000')}, 'text': '13,986,353.82'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('377.810000'), 'w': Decimal('42.143000'), 'r': Decimal('95.893000'),
        'h': Decimal('11.510000')}, 'text': ''}, {'pos': {'x': Decimal('96.260000'), 'y': Decimal('377.810000'),
                                                          'w': Decimal('482.610000'), 'r': Decimal('578.870000'),
                                                          'h': Decimal('11.510000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('365.810000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('365.810000'),
                                                          'w': Decimal('489.450000'), 'r': Decimal('578.994000'),
                                                          'h': Decimal('11.990000')}, 'text': '5.5.2.4其他应收款坏账准备计提情况'}],
    [{
        'pos': {
            'x': Decimal(
                '53.750000'),
            'y': Decimal(
                '353.810000'),
            'w': Decimal(
                '35.303000'),
            'r': Decimal(
                '89.053000'),
            'h': Decimal(
                '11.990000')},
        'text': ''},
        {
            'pos': {
                'x': Decimal(
                    '89.544000'),
                'y': Decimal(
                    '353.810000'),
                'w': Decimal(
                    '489.450000'),
                'r': Decimal(
                    '578.994000'),
                'h': Decimal(
                    '11.990000')},
            'text': ''}],
    [{'pos': {'x': Decimal('53.750000'), 'y': Decimal('341.810000'), 'w': Decimal('35.303000'),
              'r': Decimal('89.053000'),
              'h': Decimal('11.990000')}, 'text': ''}, {
         'pos': {'x': Decimal('89.544000'), 'y': Decimal('305.330000'), 'w': Decimal('141.613000'),
                 'r': Decimal('231.157000'), 'h': Decimal('48.470000')}, 'text': '坏账准备'}, {
         'pos': {'x': Decimal('231.050000'), 'y': Decimal('341.810000'), 'w': Decimal('14.160000'),
                 'r': Decimal('245.210000'), 'h': Decimal('11.990000')}, 'text': ''}, {
         'pos': {'x': Decimal('246.050000'), 'y': Decimal('341.810000'), 'w': Decimal('70.920000'),
                 'r': Decimal('316.970000'), 'h': Decimal('11.990000')}, 'text': '第一阶段'}, {
         'pos': {'x': Decimal('316.730000'), 'y': Decimal('341.810000'), 'w': Decimal('14.544000'),
                 'r': Decimal('331.274000'), 'h': Decimal('11.990000')}, 'text': ''}, {
         'pos': {'x': Decimal('329.960000'), 'y': Decimal('341.810000'), 'w': Decimal('77.990000'),
                 'r': Decimal('407.950000'), 'h': Decimal('11.990000')}, 'text': '第二阶段'}, {
         'pos': {'x': Decimal('409.520000'), 'y': Decimal('341.810000'), 'w': Decimal('14.150000'),
                 'r': Decimal('423.670000'), 'h': Decimal('11.990000')}, 'text': ''}, {
         'pos': {'x': Decimal('423.910000'), 'y': Decimal('341.810000'), 'w': Decimal('77.894000'),
                 'r': Decimal('501.804000'), 'h': Decimal('11.990000')}, 'text': '第三阶段'}, {
         'pos': {'x': Decimal('501.700000'), 'y': Decimal('341.810000'), 'w': Decimal('14.150000'),
                 'r': Decimal('515.850000'), 'h': Decimal('11.990000')}, 'text': ''}, {
         'pos': {'x': Decimal('515.140000'), 'y': Decimal('305.330000'), 'w': Decimal('63.980000'),
                 'r': Decimal('579.120000'), 'h': Decimal('48.470000')}, 'text': '合计'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('305.330000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('35.990000')}, 'text': ''}, {'pos': {'x': Decimal('231.050000'), 'y': Decimal('305.330000'),
                                                          'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
                                                          'h': Decimal('35.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('246.050000'), 'y': Decimal('305.330000'), 'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
        'h': Decimal('35.990000')}, 'text': '未来12个月预期信用损失'}, {'pos': {'x': Decimal('316.730000'),
                                                                      'y': Decimal('305.330000'),
                                                                      'w': Decimal('14.544000'),
                                                                      'r': Decimal('331.274000'),
                                                                      'h': Decimal('35.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('329.960000'), 'y': Decimal('305.330000'), 'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
        'h': Decimal('35.990000')}, 'text': '整个存续期预期信用损失（未发生信用减值）'}, {'pos': {'x': Decimal('409.520000'),
                                                                              'y': Decimal('305.330000'),
                                                                              'w': Decimal('14.150000'),
                                                                              'r': Decimal('423.670000'),
                                                                              'h': Decimal('35.990000')}, 'text': ''}, {
        'pos': {'x': Decimal(
            '423.910000'),
            'y': Decimal(
                '305.330000'),
            'w': Decimal(
                '77.894000'),
            'r': Decimal(
                '501.804000'),
            'h': Decimal(
                '35.990000')},
        'text': '整个存续期预期信用损失（已发生信用减值）'},
        {'pos': {
            'x': Decimal('501.700000'),
            'y': Decimal('305.330000'),
            'w': Decimal('14.150000'),
            'r': Decimal('515.850000'),
            'h': Decimal('35.990000')},
            'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('292.850000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('292.850000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '2019年1月1日余额'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('292.850000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('292.850000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': '29,044.00'}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('292.850000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('292.850000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('292.850000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('292.850000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': '3,115,840.59'}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('292.850000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('292.850000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': '3,144,884.59'}],
    [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('280.850000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('280.850000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '2019年1月1日余额在本期'},
        {'pos': {
            'x': Decimal('231.050000'), 'y': Decimal('280.850000'), 'w': Decimal('14.160000'),
            'r': Decimal('245.210000'),
            'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('280.850000'),
                                                              'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                              'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('280.850000'), 'w': Decimal('14.544000'),
        'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('280.850000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('280.850000'), 'w': Decimal('14.150000'),
        'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('280.850000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('280.850000'), 'w': Decimal('14.150000'),
        'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('280.850000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('268.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('12.014000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('268.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('12.014000')}, 'text': '--转入第二阶段'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('268.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('12.014000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('268.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('12.014000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('268.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('12.014000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('268.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('12.014000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('268.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('12.014000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('268.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('12.014000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('268.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('12.014000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('268.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('12.014000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('256.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('256.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '--转入第三阶段'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('256.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('256.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('256.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('256.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('256.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('256.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('256.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('256.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('244.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('244.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '--转回第二阶段'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('244.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('244.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('244.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('244.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('244.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('244.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('244.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('244.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('232.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('232.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '--转回第一阶段'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('232.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('232.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('232.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('232.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('232.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('232.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('232.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('232.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('220.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('220.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '本期计提'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('220.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('220.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('220.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('220.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('220.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('220.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': '1,018,859.04'}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('220.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('220.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': '1,018,859.04'}],
    [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('208.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('208.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '本期转回'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('208.830000'), 'w': Decimal('14.160000'),
        'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('208.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': '19,984.00'}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('208.830000'), 'w': Decimal('14.544000'),
        'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('208.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('208.830000'), 'w': Decimal('14.150000'),
        'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('208.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('208.830000'), 'w': Decimal('14.150000'),
        'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('208.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': '19,984.00'}],
    [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('196.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('196.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '本期转销'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('196.830000'), 'w': Decimal('14.160000'),
        'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('196.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('196.830000'), 'w': Decimal('14.544000'),
        'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('196.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('196.830000'), 'w': Decimal('14.150000'),
        'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('196.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('196.830000'), 'w': Decimal('14.150000'),
        'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('196.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('184.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('184.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '本期核销'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('184.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('184.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('184.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('184.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('184.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('184.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('184.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('184.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('172.830000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('172.830000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '其他变动'}, {'pos': {
        'x': Decimal('231.050000'), 'y': Decimal('172.830000'), 'w': Decimal('14.160000'), 'r': Decimal('245.210000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('172.830000'),
                                                          'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('316.730000'), 'y': Decimal('172.830000'), 'w': Decimal('14.544000'), 'r': Decimal('331.274000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('172.830000'),
                                                          'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('409.520000'), 'y': Decimal('172.830000'), 'w': Decimal('14.150000'), 'r': Decimal('423.670000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('172.830000'),
                                                          'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
        'x': Decimal('501.700000'), 'y': Decimal('172.830000'), 'w': Decimal('14.150000'), 'r': Decimal('515.850000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('172.830000'),
                                                          'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('160.230000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('160.230000'),
                                                          'w': Decimal('141.613000'), 'r': Decimal('231.157000'),
                                                          'h': Decimal('11.990000')}, 'text': '2019年12月31日余额'},
        {'pos': {
            'x': Decimal('231.050000'), 'y': Decimal('160.230000'), 'w': Decimal('14.160000'),
            'r': Decimal('245.210000'),
            'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('246.050000'), 'y': Decimal('160.230000'),
                                                              'w': Decimal('70.920000'), 'r': Decimal('316.970000'),
                                                              'h': Decimal('11.990000')}, 'text': '9,060.00'},
        {'pos': {
            'x': Decimal('316.730000'), 'y': Decimal('160.230000'), 'w': Decimal('14.544000'),
            'r': Decimal('331.274000'),
            'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('329.960000'), 'y': Decimal('160.230000'),
                                                              'w': Decimal('77.990000'), 'r': Decimal('407.950000'),
                                                              'h': Decimal('11.990000')}, 'text': ''}, {'pos': {
            'x': Decimal('409.520000'), 'y': Decimal('160.230000'), 'w': Decimal('14.150000'),
            'r': Decimal('423.670000'),
            'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('423.910000'), 'y': Decimal('160.230000'),
                                                              'w': Decimal('77.894000'), 'r': Decimal('501.804000'),
                                                              'h': Decimal('11.990000')}, 'text': '4,134,699.63'},
        {'pos': {
            'x': Decimal('501.700000'), 'y': Decimal('160.230000'), 'w': Decimal('14.150000'),
            'r': Decimal('515.850000'),
            'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('515.140000'), 'y': Decimal('160.230000'),
                                                              'w': Decimal('63.980000'), 'r': Decimal('579.120000'),
                                                              'h': Decimal('11.990000')}, 'text': '4,143,759.63'}],
    [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('146.790000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('146.790000'),
                                                          'w': Decimal('489.450000'), 'r': Decimal('578.994000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('134.790000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('134.790000'),
                                                          'w': Decimal('489.450000'), 'r': Decimal('578.994000'),
                                                          'h': Decimal('11.990000')},
                                                  'text': '按组合计提坏账的确认标准及说明：详见财务报表附注3.10.7。'}], [{'pos': {
        'x': Decimal('53.750000'), 'y': Decimal('122.790000'), 'w': Decimal('35.303000'), 'r': Decimal('89.053000'),
        'h': Decimal('11.990000')}, 'text': ''}, {'pos': {'x': Decimal('89.544000'), 'y': Decimal('122.790000'),
                                                          'w': Decimal('489.450000'), 'r': Decimal('578.994000'),
                                                          'h': Decimal('11.990000')}, 'text': ''}]]
