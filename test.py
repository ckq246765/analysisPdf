#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from decimal import Decimal

[{'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('776.160000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('758.500000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('231.050000'), 'h': Decimal('42.013125'), 'y': Decimal('631.900000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('231.050000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('618.100000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('602.500000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('586.870000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('571.270000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('555.670000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('540.070000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('524.470000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('508.870000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('493.270000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('477.670000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('462.070000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('525.100000'), 'h': Decimal('42.013125'), 'y': Decimal('278.090000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('525.100000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('259.220000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('243.620000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('228.020000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('212.420000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('196.820000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('181.220000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('165.620000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('150.020000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '2019', 'table_name': '',
  'style_dict': {'x': Decimal('415.270000'), 'h': Decimal('98.158594'), 'y': Decimal('112.340000'),
                 'fs': Decimal('104.160000'), 'w': Decimal('0.000000'), 'r': Decimal('415.270000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('46.507500'), 'y': Decimal('78.360000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '大泽电极NEEQ：832850',
  'style_dict': {'x': Decimal('313.880000'), 'y': Decimal('637.180000'), 'w': Decimal('218.180000'),
                 'r': Decimal('532.060000'), 'h': Decimal('108.470000')}},
 {'el_type': 'table', 'table_name': '云南大泽电极科技股份有限公司YunnanDazeElecrtodeTechnology年度报告', 'table_data': [[{'pos': {
     'x': Decimal('66.991000'), 'y': Decimal('489.310000'), 'w': Decimal('464.580000'), 'r': Decimal('531.571000'),
     'h': Decimal('95.760000')}, 'text': '云南大泽电极科技股份有限公司YunnanDazeElecrtodeTechnology'}, {'pos': {
     'x': Decimal('362.840000'), 'y': Decimal('156.150000'), 'w': Decimal('164.650000'), 'r': Decimal('527.490000'),
     'h': Decimal('44.990000')}, 'text': '年度报告'}]]}, {'el_type': 'p', 'text': '公司年度大事记', 'table_name': '',
                                                      'style_dict': {'x': Decimal('248.570000'),
                                                                     'h': Decimal('73.722656'),
                                                                     'y': Decimal('743.260000'),
                                                                     'fs': Decimal('56.160000'),
                                                                     'w': Decimal('0.000000'),
                                                                     'r': Decimal('248.570000')}},
 {'el_type': 'table', 'text': '', 'table_name': '公司年度大事记', 'table_data': [],
  'style_dict': {'x': Decimal('89.544000'), 'h': Decimal('55.858359'), 'y': Decimal('642.940000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('89.544000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('132.980000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('117.380000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '目录', 'table_name': '',
  'style_dict': {'x': Decimal('279.770000'), 'h': Decimal('59.625000'), 'y': Decimal('747.820000'),
                 'fs': Decimal('72.000000'), 'w': Decimal('0.000000'), 'r': Decimal('279.770000')}}, {'el_type': 'p',
                                                                                                      'text': '第一节声明与提示....................................................................................................................5',
                                                                                                      'table_name': '',
                                                                                                      'style_dict': {
                                                                                                          'x': Decimal(
                                                                                                              '61.560000'),
                                                                                                          'h': Decimal(
                                                                                                              '47.742188'),
                                                                                                          'y': Decimal(
                                                                                                              '708.700000'),
                                                                                                          'fs': Decimal(
                                                                                                              '48.000000'),
                                                                                                          'w': Decimal(
                                                                                                              '0.000000'),
                                                                                                          'r': Decimal(
                                                                                                              '61.560000')}},
 {'el_type': 'p',
  'text': '第二节公司概况........................................................................................................................7',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('675.100000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第三节会计数据和财务指标摘要............................................................................................9',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('641.500000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第四节管理层讨论与分析......................................................................................................11',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('607.900000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第五节重要事项......................................................................................................................30',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('574.270000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第六节股本变动及股东情况..................................................................................................37',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('540.670000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第七节融资及利润分配情况..................................................................................................39',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('507.070000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '第八节董事、监事、高级管理人员及员工情况..................................................................41',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('473.470000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第九节行业信息......................................................................................................................44',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('439.870000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第十节公司治理及内部控制..................................................................................................45',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('406.250000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p',
  'text': '第十一节财务报告...................................................................................................................50',
  'table_name': '', 'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('47.742188'), 'y': Decimal('372.650000'),
                                   'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('297.770000'), 'h': Decimal('59.625000'), 'y': Decimal('328.970000'),
                 'fs': Decimal('72.000000'), 'w': Decimal('0.000000'), 'r': Decimal('297.770000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('73.584000'), 'h': Decimal('38.367188'), 'y': Decimal('299.570000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('73.584000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '释义', 'table_name': '',
  'style_dict': {'x': Decimal('283.730000'), 'h': Decimal('46.507500'), 'y': Decimal('749.260000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('283.730000')}},
 {'el_type': 'table', 'table_name': '西部矿业指西部矿业股份有限公司锌业分公司', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('663.820000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('569.230000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.415000')},
                                                                             'text': '2019年5月，完成“100户云南省民营小巨人”企业复核工作，继2016年首次认定以来，再次获得云南省工信委的认定。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('443.350000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('93.600000')},
                                                                             'text': '2019年7月10日，设立全资子公司汉中大泽科技有限公司，以“一对一”的方式和整套技术服务方案与客户建立长期稳定的战略合作关系，进一步拓展公司的发展空间。截止目前，已成功对外设立4个生产基地。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('286.370000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('124.790000')},
                                                                             'text': '公司推崇绿色节能生产的理念，建立的“多元合金阴阳极板生产过程所涉及的能源管理活动及节能技术应用”符合GB/T23331-2012/ISO50001:2011及RB/T117-2014《能源管理体系有色金属企业认证要求》，2019年11月，获得能源管理体系认证证书。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('191.790000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '公司注重专利技术保护，2019年度，共向国家知识产权局申请实用新型、发明专利30余项，现已获受理，并进入实质审查阶段。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('722.620000'),
                                                                                     'w': Decimal('191.329000'),
                                                                                     'r': Decimal('247.358000'),
                                                                                     'h': Decimal('15.590000')},
                                                                             'text': '释义项目'}, {
                                                                                'pos': {'x': Decimal('248.570000'),
                                                                                        'y': Decimal('722.620000'),
                                                                                        'w': Decimal('35.040000'),
                                                                                        'r': Decimal('283.610000'),
                                                                                        'h': Decimal('15.590000')},
                                                                                'text': ''}, {
                                                                                'pos': {'x': Decimal('283.730000'),
                                                                                        'y': Decimal('722.620000'),
                                                                                        'w': Decimal('255.410000'),
                                                                                        'r': Decimal('539.140000'),
                                                                                        'h': Decimal('15.590000')},
                                                                                'text': '释义'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
     'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                       'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                       'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
     'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('663.820000'),
                                                                                             'w': Decimal('482.730000'),
                                                                                             'r': Decimal('538.759000'),
                                                                                             'h': Decimal('62.390000')},
                                                                                     'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                               {'pos': {'x': Decimal(
                                                                                   '56.029000'),
                                                                                   'y': Decimal(
                                                                                       '663.820000'),
                                                                                   'w': Decimal(
                                                                                       '482.730000'),
                                                                                   'r': Decimal(
                                                                                       '538.759000'),
                                                                                   'h': Decimal(
                                                                                       '62.390000')},
                                                                                   'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                               {'pos': {'x': Decimal(
                                                                                   '56.029000'),
                                                                                   'y': Decimal(
                                                                                       '706.540000'),
                                                                                   'w': Decimal(
                                                                                       '191.329000'),
                                                                                   'r': Decimal(
                                                                                       '247.358000'),
                                                                                   'h': Decimal(
                                                                                       '15.590000')},
                                                                                   'text': '本公司、公司、大泽电极'},
                                                                               {'pos': {'x': Decimal(
                                                                                   '248.570000'),
                                                                                   'y': Decimal(
                                                                                       '706.540000'),
                                                                                   'w': Decimal(
                                                                                       '35.040000'),
                                                                                   'r': Decimal(
                                                                                       '283.610000'),
                                                                                   'h': Decimal(
                                                                                       '15.590000')},
                                                                                   'text': '指'}, {
         'pos': {
             'x': Decimal(
                 '283.730000'),
             'y': Decimal(
                 '706.540000'),
             'w': Decimal(
                 '255.410000'),
             'r': Decimal(
                 '539.140000'),
             'h': Decimal(
                 '15.590000')},
         'text': '云南大泽电极科技股份有限公司'}],
                                                                           [{'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('443.350000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('93.600000')},
                                                                             'text': ''}, {
                                                                                'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('663.820000'),
                                                                                        'w': Decimal('482.730000'),
                                                                                        'r': Decimal('538.759000'),
                                                                                        'h': Decimal('62.390000')},
                                                                                'text': ''}, {
                                                                                'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('663.820000'),
                                                                                        'w': Decimal('482.730000'),
                                                                                        'r': Decimal('538.759000'),
                                                                                        'h': Decimal('62.390000')},
                                                                                'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('663.820000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('663.820000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('690.460000'),
                                                                                     'w': Decimal('191.329000'),
                                                                                     'r': Decimal('247.358000'),
                                                                                     'h': Decimal('15.590000')},
                                                                             'text': '控股子公司、内蒙古大泽'}, {
                                                                                'pos': {'x': Decimal('248.570000'),
                                                                                        'y': Decimal('690.460000'),
                                                                                        'w': Decimal('35.040000'),
                                                                                        'r': Decimal('283.610000'),
                                                                                        'h': Decimal('15.590000')},
                                                                                'text': '指'}, {
                                                                                'pos': {'x': Decimal('283.730000'),
                                                                                        'y': Decimal('690.460000'),
                                                                                        'w': Decimal('255.410000'),
                                                                                        'r': Decimal('539.140000'),
                                                                                        'h': Decimal('15.590000')},
                                                                                'text': '内蒙古大泽电极科技有限公司'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('674.260000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.590000')}, 'text': '全资子公司、赤峰大泽'}, {'pos': {'x': Decimal('248.570000'),
                                                                     'y': Decimal('674.260000'),
                                                                     'w': Decimal('35.040000'),
                                                                     'r': Decimal('283.610000'),
                                                                     'h': Decimal('15.590000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('674.260000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.590000')}, 'text': '赤峰大泽科技有限公司'}], [{'pos': {'x': Decimal('56.029000'),
                                                                       'y': Decimal('443.350000'),
                                                                       'w': Decimal('482.730000'),
                                                                       'r': Decimal('538.759000'),
                                                                       'h': Decimal('93.600000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('658.180000'),
                                                                          'w': Decimal('191.329000'),
                                                                          'r': Decimal('247.358000'),
                                                                          'h': Decimal('15.590000')},
                                                                  'text': '分公司、水口山分公司'}, {
                                                                  'pos': {'x': Decimal('248.570000'),
                                                                          'y': Decimal('658.180000'),
                                                                          'w': Decimal('35.040000'),
                                                                          'r': Decimal('283.610000'),
                                                                          'h': Decimal('15.590000')}, 'text': '指'}, {
                                                                  'pos': {'x': Decimal('283.730000'),
                                                                          'y': Decimal('658.180000'),
                                                                          'w': Decimal('255.410000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('15.590000')},
                                                                  'text': '云南大泽电极科技股份有限公司水口山分公司'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('642.100000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.590000')}, 'text': '全资子公司、汉中大泽'}, {'pos': {'x': Decimal('248.570000'),
                                                                     'y': Decimal('642.100000'),
                                                                     'w': Decimal('35.040000'),
                                                                     'r': Decimal('283.610000'),
                                                                     'h': Decimal('15.590000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('642.100000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.590000')}, 'text': '汉中大泽科技有限公司'}], [{'pos': {'x': Decimal('56.029000'),
                                                                       'y': Decimal('443.350000'),
                                                                       'w': Decimal('482.730000'),
                                                                       'r': Decimal('538.759000'),
                                                                       'h': Decimal('93.600000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('626.020000'),
                                                                          'w': Decimal('191.329000'),
                                                                          'r': Decimal('247.358000'),
                                                                          'h': Decimal('15.590000')},
                                                                  'text': '主办券商、东北证券'}, {
                                                                  'pos': {'x': Decimal('248.570000'),
                                                                          'y': Decimal('626.020000'),
                                                                          'w': Decimal('35.040000'),
                                                                          'r': Decimal('283.610000'),
                                                                          'h': Decimal('15.590000')}, 'text': '指'}, {
                                                                  'pos': {'x': Decimal('283.730000'),
                                                                          'y': Decimal('626.020000'),
                                                                          'w': Decimal('255.410000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('15.590000')},
                                                                  'text': '东北证券股份有限公司'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('609.940000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.590000')}, 'text': '会计师事务所'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('609.940000'),
                                                                 'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                                 'h': Decimal('15.590000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('609.940000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.590000')}, 'text': '众华会计师事务所（特殊普通合伙）'}], [{'pos': {'x': Decimal('56.029000'),
                                                                             'y': Decimal('443.350000'),
                                                                             'w': Decimal('482.730000'),
                                                                             'r': Decimal('538.759000'),
                                                                             'h': Decimal('93.600000')}, 'text': ''}, {
                                                                        'pos': {'x': Decimal('56.029000'),
                                                                                'y': Decimal('663.820000'),
                                                                                'w': Decimal('482.730000'),
                                                                                'r': Decimal('538.759000'),
                                                                                'h': Decimal('62.390000')}, 'text': ''},
                                                                    {'pos': {'x': Decimal('56.029000'),
                                                                             'y': Decimal('663.820000'),
                                                                             'w': Decimal('482.730000'),
                                                                             'r': Decimal('538.759000'),
                                                                             'h': Decimal('62.390000')},
                                                                     'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                    {'pos': {'x': Decimal('56.029000'),
                                                                             'y': Decimal('663.820000'),
                                                                             'w': Decimal('482.730000'),
                                                                             'r': Decimal('538.759000'),
                                                                             'h': Decimal('62.390000')},
                                                                     'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                    {'pos': {'x': Decimal('56.029000'),
                                                                             'y': Decimal('663.820000'),
                                                                             'w': Decimal('482.730000'),
                                                                             'r': Decimal('538.759000'),
                                                                             'h': Decimal('62.390000')},
                                                                     'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                    {'pos': {'x': Decimal('56.029000'),
                                                                             'y': Decimal('593.830000'),
                                                                             'w': Decimal('191.329000'),
                                                                             'r': Decimal('247.358000'),
                                                                             'h': Decimal('15.615000')}, 'text': '报告期'},
                                                                    {'pos': {'x': Decimal('248.570000'),
                                                                             'y': Decimal('593.830000'),
                                                                             'w': Decimal('35.040000'),
                                                                             'r': Decimal('283.610000'),
                                                                             'h': Decimal('15.615000')}, 'text': '指'}, {
                                                                        'pos': {'x': Decimal('283.730000'),
                                                                                'y': Decimal('593.830000'),
                                                                                'w': Decimal('255.410000'),
                                                                                'r': Decimal('539.140000'),
                                                                                'h': Decimal('15.615000')},
                                                                        'text': '2019年1月1日至2019年12月31日'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('577.630000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.600000')}, 'text': '报告期初'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('577.630000'),
                                                               'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                               'h': Decimal('15.600000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('577.630000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.600000')}, 'text': '2019年1月1日'}], [{'pos': {'x': Decimal('56.029000'),
                                                                      'y': Decimal('443.350000'),
                                                                      'w': Decimal('482.730000'),
                                                                      'r': Decimal('538.759000'),
                                                                      'h': Decimal('93.600000')}, 'text': ''}, {
                                                                 'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('663.820000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('62.390000')}, 'text': ''}, {
                                                                 'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('663.820000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('62.390000')},
                                                                 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                 'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('663.820000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('62.390000')},
                                                                 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                 'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('663.820000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('62.390000')},
                                                                 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                 'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('561.550000'),
                                                                         'w': Decimal('191.329000'),
                                                                         'r': Decimal('247.358000'),
                                                                         'h': Decimal('15.600000')}, 'text': '报告期末'}, {
                                                                 'pos': {'x': Decimal('248.570000'),
                                                                         'y': Decimal('561.550000'),
                                                                         'w': Decimal('35.040000'),
                                                                         'r': Decimal('283.610000'),
                                                                         'h': Decimal('15.600000')}, 'text': '指'}, {
                                                                 'pos': {'x': Decimal('283.730000'),
                                                                         'y': Decimal('561.550000'),
                                                                         'w': Decimal('255.410000'),
                                                                         'r': Decimal('539.140000'),
                                                                         'h': Decimal('15.600000')},
                                                                 'text': '2019年12月31日'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('545.470000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.600000')}, 'text': '三会'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('545.470000'),
                                                             'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                             'h': Decimal('15.600000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('545.470000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.600000')}, 'text': '股东大会、董事会、监事会'}], [{'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('443.350000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('93.600000')}, 'text': ''}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')}, 'text': ''}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('529.390000'),
                                                                            'w': Decimal('191.329000'),
                                                                            'r': Decimal('247.358000'),
                                                                            'h': Decimal('15.600000')}, 'text': '股东大会'},
                                                                {'pos': {'x': Decimal('248.570000'),
                                                                         'y': Decimal('529.390000'),
                                                                         'w': Decimal('35.040000'),
                                                                         'r': Decimal('283.610000'),
                                                                         'h': Decimal('15.600000')}, 'text': '指'}, {
                                                                    'pos': {'x': Decimal('283.730000'),
                                                                            'y': Decimal('529.390000'),
                                                                            'w': Decimal('255.410000'),
                                                                            'r': Decimal('539.140000'),
                                                                            'h': Decimal('15.600000')},
                                                                    'text': '云南大泽电极科技股份有限公司股东大会'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('513.310000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.600000')}, 'text': '元、万元'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('513.310000'),
                                                               'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                               'h': Decimal('15.600000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('513.310000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.600000')}, 'text': '人民币元、人民币万元'}], [{'pos': {'x': Decimal('56.029000'),
                                                                       'y': Decimal('443.350000'),
                                                                       'w': Decimal('482.730000'),
                                                                       'r': Decimal('538.759000'),
                                                                       'h': Decimal('93.600000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('466.030000'),
                                                                          'w': Decimal('191.329000'),
                                                                          'r': Decimal('247.358000'),
                                                                          'h': Decimal('46.800000')}, 'text': '湿法冶金'}, {
                                                                  'pos': {'x': Decimal('248.570000'),
                                                                          'y': Decimal('466.030000'),
                                                                          'w': Decimal('35.040000'),
                                                                          'r': Decimal('283.610000'),
                                                                          'h': Decimal('46.800000')}, 'text': '指'}, {
                                                                  'pos': {'x': Decimal('283.730000'),
                                                                          'y': Decimal('466.030000'),
                                                                          'w': Decimal('255.410000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('46.800000')},
                                                                  'text': '湿法冶金就是金属矿物原料在酸性介质或碱性介质的水溶液中进行化学处理或有机溶剂萃取、分离杂质、提取金属及其化合物的过程'}],
                                                                           [{'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('443.350000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('93.600000')},
                                                                             'text': ''}, {
                                                                                'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('663.820000'),
                                                                                        'w': Decimal('482.730000'),
                                                                                        'r': Decimal('538.759000'),
                                                                                        'h': Decimal('62.390000')},
                                                                                'text': ''}, {
                                                                                'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('663.820000'),
                                                                                        'w': Decimal('482.730000'),
                                                                                        'r': Decimal('538.759000'),
                                                                                        'h': Decimal('62.390000')},
                                                                                'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('663.820000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('663.820000'),
                                                                                     'w': Decimal('482.730000'),
                                                                                     'r': Decimal('538.759000'),
                                                                                     'h': Decimal('62.390000')},
                                                                             'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'},
                                                                            {'pos': {'x': Decimal('56.029000'),
                                                                                     'y': Decimal('449.830000'),
                                                                                     'w': Decimal('191.329000'),
                                                                                     'r': Decimal('247.358000'),
                                                                                     'h': Decimal('15.600000')},
                                                                             'text': '云锡华联锌铟'}, {
                                                                                'pos': {'x': Decimal('248.570000'),
                                                                                        'y': Decimal('449.830000'),
                                                                                        'w': Decimal('35.040000'),
                                                                                        'r': Decimal('283.610000'),
                                                                                        'h': Decimal('15.600000')},
                                                                                'text': '指'}, {
                                                                                'pos': {'x': Decimal('283.730000'),
                                                                                        'y': Decimal('449.830000'),
                                                                                        'w': Decimal('255.410000'),
                                                                                        'r': Decimal('539.140000'),
                                                                                        'h': Decimal('15.600000')},
                                                                                'text': '云锡文山锌铟冶炼有限公司'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('433.750000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.600000')}, 'text': '万邦物流'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('433.750000'),
                                                               'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                               'h': Decimal('15.600000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('433.750000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.600000')}, 'text': '北方万邦物流有限公司'}], [{'pos': {'x': Decimal('56.029000'),
                                                                       'y': Decimal('443.350000'),
                                                                       'w': Decimal('482.730000'),
                                                                       'r': Decimal('538.759000'),
                                                                       'h': Decimal('93.600000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')}, 'text': ''}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('663.820000'),
                                                                          'w': Decimal('482.730000'),
                                                                          'r': Decimal('538.759000'),
                                                                          'h': Decimal('62.390000')},
                                                                  'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                  'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('417.650000'),
                                                                          'w': Decimal('191.329000'),
                                                                          'r': Decimal('247.358000'),
                                                                          'h': Decimal('15.590000')}, 'text': '中金岭南'}, {
                                                                  'pos': {'x': Decimal('248.570000'),
                                                                          'y': Decimal('417.650000'),
                                                                          'w': Decimal('35.040000'),
                                                                          'r': Decimal('283.610000'),
                                                                          'h': Decimal('15.590000')}, 'text': '指'}, {
                                                                  'pos': {'x': Decimal('283.730000'),
                                                                          'y': Decimal('417.650000'),
                                                                          'w': Decimal('255.410000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('15.590000')},
                                                                  'text': '深圳市中金岭南有色金属股份有限公司丹霞冶炼厂'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('401.570000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.590000')}, 'text': '湖南株冶'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('401.570000'),
                                                               'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                               'h': Decimal('15.590000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('401.570000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.590000')}, 'text': '湖南株冶有色金属有限公司'}], [{'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('443.350000'),
                                                                         'w': Decimal('482.730000'),
                                                                         'r': Decimal('538.759000'),
                                                                         'h': Decimal('93.600000')}, 'text': ''}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')}, 'text': ''}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('663.820000'),
                                                                            'w': Decimal('482.730000'),
                                                                            'r': Decimal('538.759000'),
                                                                            'h': Decimal('62.390000')},
                                                                    'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {
                                                                    'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('385.490000'),
                                                                            'w': Decimal('191.329000'),
                                                                            'r': Decimal('247.358000'),
                                                                            'h': Decimal('15.590000')}, 'text': '天津茂联'},
                                                                {'pos': {'x': Decimal('248.570000'),
                                                                         'y': Decimal('385.490000'),
                                                                         'w': Decimal('35.040000'),
                                                                         'r': Decimal('283.610000'),
                                                                         'h': Decimal('15.590000')}, 'text': '指'}, {
                                                                    'pos': {'x': Decimal('283.730000'),
                                                                            'y': Decimal('385.490000'),
                                                                            'w': Decimal('255.410000'),
                                                                            'r': Decimal('539.140000'),
                                                                            'h': Decimal('15.590000')},
                                                                    'text': '天津市茂联科技有限公司'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('443.350000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('93.600000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('663.820000'),
                                                           'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
                                                           'h': Decimal('62.390000')}, 'text': ''}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('663.820000'), 'w': Decimal('482.730000'), 'r': Decimal('538.759000'),
         'h': Decimal('62.390000')}, 'text': '2019年5月公司达到创新层维持标准，自2016年起连续4年列入创新层企业。'}, {'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('369.410000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
         'h': Decimal('15.590000')}, 'text': '西部矿业'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('369.410000'),
                                                               'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                               'h': Decimal('15.590000')}, 'text': '指'}, {'pos': {
         'x': Decimal('283.730000'), 'y': Decimal('369.410000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
         'h': Decimal('15.590000')}, 'text': '西部矿业股份有限公司锌业分公司'}]]}, {'el_type': 'p', 'text': '', 'table_name': '',
                                                                     'style_dict': {'x': Decimal('61.560000'),
                                                                                    'h': Decimal('42.013125'),
                                                                                    'y': Decimal('325.730000'),
                                                                                    'fs': Decimal('42.240000'),
                                                                                    'w': Decimal('0.000000'),
                                                                                    'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('310.130000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '第一节声明与提示', 'table_name': '',
  'style_dict': {'x': Decimal('231.050000'), 'h': Decimal('57.503672'), 'y': Decimal('743.260000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('231.050000')}},
 {'el_type': 'p', 'text': '【声明】', 'table_name': '',
  'style_dict': {'x': Decimal('82.584000'), 'h': Decimal('35.145000'), 'y': Decimal('711.220000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('82.584000')}},
 {'el_type': 'p', 'text': '公司控股股东、实际控制人、董事、监事、高级管理人员保证本报告所载资料不存在任何虚假记载、误', 'table_name': '',
  'style_dict': {'x': Decimal('82.584000'), 'h': Decimal('35.145000'), 'y': Decimal('687.820000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('82.584000')}},
 {'el_type': 'p', 'text': '导性陈述或者重大遗漏，并对其内容的真实性、准确性和完整性承担个别及连带责任。', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.145000'), 'y': Decimal('664.420000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('441.670000'), 'h': Decimal('42.013125'), 'y': Decimal('664.660000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('441.670000')}},
 {'el_type': 'p', 'text': '公司负责人张国义、主管会计工作负责人张国义及会计机构负责人（会计主管人员）吴蓉保证年度', 'table_name': '',
  'style_dict': {'x': Decimal('82.584000'), 'h': Decimal('35.145000'), 'y': Decimal('641.020000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('82.584000')}},
 {'el_type': 'p', 'text': '报告中财务报告的真实、准确、完整。', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.145000'), 'y': Decimal('617.620000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('240.170000'), 'h': Decimal('42.013125'), 'y': Decimal('617.860000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('240.170000')}},
 {'el_type': 'p', 'text': '众华会计师事务所', 'table_name': '',
  'style_dict': {'x': Decimal('82.584000'), 'h': Decimal('35.145000'), 'y': Decimal('594.190000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('82.584000')}},
 {'el_type': 'p', 'text': '(', 'table_name': '',
  'style_dict': {'x': Decimal('166.700000'), 'h': Decimal('42.013125'), 'y': Decimal('594.430000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('166.700000')}},
 {'el_type': 'p', 'text': '特殊普通合伙', 'table_name': '',
  'style_dict': {'x': Decimal('169.820000'), 'h': Decimal('35.145000'), 'y': Decimal('594.190000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('169.820000')}},
 {'el_type': 'p', 'text': ')', 'table_name': '',
  'style_dict': {'x': Decimal('232.850000'), 'h': Decimal('42.013125'), 'y': Decimal('594.430000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('232.850000')}},
 {'el_type': 'p', 'text': '对公司出具了标准无保留意见审计报告。', 'table_name': '',
  'style_dict': {'x': Decimal('236.090000'), 'h': Decimal('35.145000'), 'y': Decimal('594.190000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('236.090000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('424.990000'), 'h': Decimal('42.013125'), 'y': Decimal('594.430000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('424.990000')}},
 {'el_type': 'p', 'text': '本年度报告涉及未来计划等前瞻性陈述，不构成公司对投资者的实质承诺，投资者及相关人士均应', 'table_name': '',
  'style_dict': {'x': Decimal('82.584000'), 'h': Decimal('35.145000'), 'y': Decimal('570.790000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('82.584000')}},
 {'el_type': 'p', 'text': '对此保持足够的风险认识，并且应当理解计划、预测与承诺之间的差异。', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.145000'), 'y': Decimal('547.390000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('397.750000'), 'h': Decimal('42.013125'), 'y': Decimal('547.630000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('397.750000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('528.070000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '是否存在未出席董事会审议年度报告的董事□是√否', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('353.210000'),
                                                                                        'w': Decimal('191.329000'),
                                                                                        'r': Decimal('247.358000'),
                                                                                        'h': Decimal('15.590000')},
                                                                                'text': '赤峰中色'}, {
                                                                                   'pos': {'x': Decimal('248.570000'),
                                                                                           'y': Decimal('353.210000'),
                                                                                           'w': Decimal('35.040000'),
                                                                                           'r': Decimal('283.610000'),
                                                                                           'h': Decimal('15.590000')},
                                                                                   'text': '指'}, {
                                                                                   'pos': {'x': Decimal('283.730000'),
                                                                                           'y': Decimal('353.210000'),
                                                                                           'w': Decimal('255.410000'),
                                                                                           'r': Decimal('539.140000'),
                                                                                           'h': Decimal('15.590000')},
                                                                                   'text': '赤峰中色锌业有限公司'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('353.210000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
     'h': Decimal('15.590000')}, 'text': '事项'}, {'pos': {'x': Decimal('248.570000'), 'y': Decimal('353.210000'),
                                                         'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                         'h': Decimal('15.590000')}, 'text': '事项'}, {'pos': {
     'x': Decimal('283.730000'), 'y': Decimal('353.210000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
     'h': Decimal('15.590000')}, 'text': '事项'}, {'pos': {'x': Decimal('437.480000'), 'y': Decimal('504.430000'),
                                                         'w': Decimal('101.650000'), 'r': Decimal('539.130000'),
                                                         'h': Decimal('18.960000')}, 'text': '是或否'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('353.210000'), 'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
     'h': Decimal('15.590000')}, 'text': '是否存在董事、监事、高级管理人员对年度报告内容异议事项或无法保证其真实、准确、完整'}, {'pos': {
     'x': Decimal('248.570000'), 'y': Decimal('353.210000'), 'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
     'h': Decimal('15.590000')}, 'text': '是否存在董事、监事、高级管理人员对年度报告内容异议事项或无法保证其真实、准确、完整'}, {'pos': {
     'x': Decimal('283.730000'), 'y': Decimal('353.210000'), 'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
     'h': Decimal('15.590000')}, 'text': '是否存在董事、监事、高级管理人员对年度报告内容异议事项或无法保证其真实、准确、完整'}, {'pos': {
     'x': Decimal('437.480000'), 'y': Decimal('472.750000'), 'w': Decimal('101.650000'), 'r': Decimal('539.130000'),
     'h': Decimal('31.200000')}, 'text': '□是√否'}], [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('353.210000'),
                                                             'w': Decimal('191.329000'), 'r': Decimal('247.358000'),
                                                             'h': Decimal('15.590000')}, 'text': '是否存在未出席董事会审议年度报告的董事'},
                                                    {'pos': {'x': Decimal('248.570000'), 'y': Decimal('353.210000'),
                                                             'w': Decimal('35.040000'), 'r': Decimal('283.610000'),
                                                             'h': Decimal('15.590000')}, 'text': '是否存在未出席董事会审议年度报告的董事'},
                                                    {'pos': {'x': Decimal('283.730000'), 'y': Decimal('353.210000'),
                                                             'w': Decimal('255.410000'), 'r': Decimal('539.140000'),
                                                             'h': Decimal('15.590000')}, 'text': '是否存在未出席董事会审议年度报告的董事'},
                                                    {'pos': {'x': Decimal('437.480000'), 'y': Decimal('456.670000'),
                                                             'w': Decimal('101.650000'), 'r': Decimal('539.130000'),
                                                             'h': Decimal('15.600000')}, 'text': '□是√否'}]]},
 {'el_type': 'p', 'text': '【重要风险提示表】', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('403.850000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('165.500000'), 'h': Decimal('49.148438'), 'y': Decimal('404.090000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('165.500000')}},
 {'el_type': 'table', 'table_name': '非经常性损益依赖的风险公司非经常性损益对政府补助有一定依赖性，若未来国家财政政策发生变动或者公司因不满足获取条件而无法获得政府补贴，公司净利润将受到不利影响。',
  'table_data': [[{'pos': {'x': Decimal('56.029000'), 'y': Decimal('440.590000'), 'w': Decimal('380.469000'),
                           'r': Decimal('436.498000'), 'h': Decimal('15.600000')}, 'text': '是否存在豁免披露事项'}, {
                      'pos': {'x': Decimal('437.480000'), 'y': Decimal('440.590000'), 'w': Decimal('101.650000'),
                              'r': Decimal('539.130000'), 'h': Decimal('15.600000')}, 'text': '□是√否'}], [{'pos': {
      'x': Decimal('56.029000'), 'y': Decimal('707.020000'), 'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
      'h': Decimal('62.420000')}, 'text': '是否存在豁免披露事项'}, {'pos': {'x': Decimal('240.170000'),
                                                                  'y': Decimal('707.020000'),
                                                                  'w': Decimal('298.010000'),
                                                                  'r': Decimal('538.180000'),
                                                                  'h': Decimal('62.420000')}, 'text': '是否存在豁免披露事项'}, {
      'pos': {
          'x': Decimal(
              '56.029000'),
          'y': Decimal(
              '380.810000'),
          'w': Decimal(
              '184.249000'),
          'r': Decimal(
              '240.278000'),
          'h': Decimal(
              '18.950000')},
      'text': '重要风险事项名称'},
                     {'pos': {
                         'x': Decimal(
                             '240.170000'),
                         'y': Decimal(
                             '380.810000'),
                         'w': Decimal(
                             '298.010000'),
                         'r': Decimal(
                             '538.180000'),
                         'h': Decimal(
                             '18.950000')},
                         'text': '重要风险事项简要描述'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('317.930000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('62.390000')}, 'text': '公司使用受到限制的资产占资产总额的比重较高'}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('380.810000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('18.950000')}, 'text': '重要风险事项名称'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('317.930000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('62.390000')},
                      'text': '报告期末，公司使用受到限制的资产占总资产的33.84%，受限资产主要为公司在银行办理贷款时做了资产质押，若公司不能按期偿还贷款,受限的土地及房产存在被银行诉讼行权的风险，将会对公司的生产经营产生不利影响。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('255.030000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('62.414000')}, 'text': '原材料价格波动风险'}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('317.930000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('62.390000')}, 'text': '公司使用受到限制的资产占资产总额的比重较高'},
                  {'pos': {'x': Decimal('240.170000'), 'y': Decimal('255.030000'), 'w': Decimal('298.010000'),
                           'r': Decimal('538.180000'), 'h': Decimal('62.414000')},
                   'text': '公司原材料包括铅、银、铜、锡等金属材料，近年,受宏观经济环境、市场供求关系以及投机资金操作的影响，金属材料价格波动较大。公司直接材料所占比例较高，如果上述主要原材料的价格大幅上涨,将会对公司的经营业绩产生不利影响。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('223.350000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('31.190000')}, 'text': '短期偿债风险'}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('255.030000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('62.414000')}, 'text': '原材料价格波动风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('223.350000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('31.190000')},
                      'text': '公司流动负债主要是短期借款，流动比率和速动比率相对较低，公司存在一定的短期偿债风险。'}], [{'pos': {'x': Decimal('56.029000'),
                                                                                        'y': Decimal('144.870000'),
                                                                                        'w': Decimal('184.249000'),
                                                                                        'r': Decimal('240.278000'),
                                                                                        'h': Decimal('77.990000')},
                                                                                'text': '资金风险'}, {
                                                                                   'pos': {'x': Decimal('56.029000'),
                                                                                           'y': Decimal('223.350000'),
                                                                                           'w': Decimal('184.249000'),
                                                                                           'r': Decimal('240.278000'),
                                                                                           'h': Decimal('31.190000')},
                                                                                   'text': '短期偿债风险'}, {
                                                                                   'pos': {'x': Decimal('240.170000'),
                                                                                           'y': Decimal('144.870000'),
                                                                                           'w': Decimal('298.010000'),
                                                                                           'r': Decimal('538.180000'),
                                                                                           'h': Decimal('77.990000')},
                                                                                   'text': '随着公司经营规模、国内区域产能战略的实施，以及产品生产对装备水平、工艺流程自动化控制水平要求的不断提高，公司对资金的需求也在不断增加。资金短缺一方面会制约公司产品和核心技术的升级；另一方面也会制约公司客户近区域产能战略的实施进度。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('81.960000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('62.424000')}, 'text': '高端人才流失风险'}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('144.870000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('77.990000')}, 'text': '资金风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('81.960000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('62.424000')},
                      'text': '公司相关的产品技术含量较高，为了保持技术上的领先性，需要不断的进行新技术和(或)新工艺的研发，对核心技术人员的依赖程度较高。如果出现核心技术泄露或核心人员流失的现象，可能会在一定程度上影响公司的市场竞争力和技术创新能力。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('514.500000'), 'w': Decimal('483.500000'),
                           'r': Decimal('539.529000'), 'h': Decimal('272.500000')}, 'text': ''}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('707.020000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('62.420000')}, 'text': '公司治理风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('707.020000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('62.420000')},
                      'text': '随着公司的快速发展，经营规模不断扩大，对公司治理将会提出更高的要求，公司治理和内部控制体系也需要在日常经营中逐渐完善。因此，公司未来经营中存在因内部管理不到位、不适应发展需要，而影响公司持续、稳定、健康发展的风险。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('707.020000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('62.420000')}, 'text': ''}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('707.020000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('62.420000')}, 'text': '公司治理风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('707.020000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('62.420000')}, 'text': ''}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('581.710000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('124.810000')},
                      'text': '受宏观经济波动及有色金属行业景气度影响的风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('581.710000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('124.810000')},
                      'text': '公司的主要业务为铅基多元合金阳极板、阴极板的生产销售，产品主要应用于有色金属湿法冶金行业。因此公司经营势必会受到有色金属供求关系变化的影响，由于有色金属行业属于与宏观经济波动密切相关的周期性行业，未来有色金属冶金行业的发展将会在很大程度上取决于外部经济、产业变化和环保要求的影响。如我国未来宏观经济发生重大变化，有色金属冶金行业出现增速减缓或负增长的情形，对公司产品服务需求下降，肯定会对公司业绩增长产生不利的影响。'}],
                 [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('534.430000'), 'w': Decimal('184.249000'),
                           'r': Decimal('240.278000'), 'h': Decimal('46.800000')}, 'text': '非经常性损益依赖的风险'}, {
                      'pos': {'x': Decimal('56.029000'), 'y': Decimal('581.710000'), 'w': Decimal('184.249000'),
                              'r': Decimal('240.278000'), 'h': Decimal('124.810000')},
                      'text': '受宏观经济波动及有色金属行业景气度影响的风险'}, {
                      'pos': {'x': Decimal('240.170000'), 'y': Decimal('534.430000'), 'w': Decimal('298.010000'),
                              'r': Decimal('538.180000'), 'h': Decimal('46.800000')},
                      'text': '公司非经常性损益对政府补助有一定依赖性，若未来国家财政政策发生变动或者公司因不满足获取条件而无法获得政府补贴，公司净利润将受到不利影响。'}]]},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('57.503672'), 'y': Decimal('478.510000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '第二节公司概况', 'table_name': '',
  'style_dict': {'x': Decimal('238.130000'), 'h': Decimal('59.625000'), 'y': Decimal('749.260000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('238.130000')}},
 {'el_type': 'p', 'text': '一、基本信息', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('718.900000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '法定代表人张国义', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                         'y': Decimal('514.990000'),
                                                                         'w': Decimal('184.249000'),
                                                                         'r': Decimal('240.278000'),
                                                                         'h': Decimal('18.840000')},
                                                                 'text': '本期重大风险是否发生重大变化：'}, {
                                                                    'pos': {'x': Decimal('240.170000'),
                                                                            'y': Decimal('514.990000'),
                                                                            'w': Decimal('298.010000'),
                                                                            'r': Decimal('538.180000'),
                                                                            'h': Decimal('18.840000')}, 'text': '否'}], [
                                                                   {'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('691.420000'),
                                                                            'w': Decimal('120.379000'),
                                                                            'r': Decimal('176.408000'),
                                                                            'h': Decimal('15.590000')},
                                                                    'text': '公司中文全称'}, {
         'pos': {'x': Decimal('177.270000'),
                 'y': Decimal('691.420000'),
                 'w': Decimal('361.860000'),
                 'r': Decimal('539.130000'),
                 'h': Decimal('15.590000')},
         'text': '云南大泽电极科技股份有限公司'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('675.340000'), 'w': Decimal('120.379000'), 'r': Decimal('176.408000'),
     'h': Decimal('15.590000')}, 'text': '英文名称及缩写'}, {'pos': {'x': Decimal('177.270000'), 'y': Decimal('675.340000'),
                                                              'w': Decimal('361.860000'), 'r': Decimal('539.130000'),
                                                              'h': Decimal('15.590000')},
                                                      'text': 'YunnanDazeElecrtodeTechnologyCo.,Ltd.'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('659.260000'), 'w': Decimal('120.379000'), 'r': Decimal('176.408000'),
     'h': Decimal('15.590000')}, 'text': '证券简称'}, {'pos': {'x': Decimal('177.270000'), 'y': Decimal('659.260000'),
                                                           'w': Decimal('361.860000'), 'r': Decimal('539.130000'),
                                                           'h': Decimal('15.590000')}, 'text': '大泽电极'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('643.060000'), 'w': Decimal('120.379000'), 'r': Decimal('176.408000'),
     'h': Decimal('15.590000')}, 'text': '证券代码'}, {'pos': {'x': Decimal('177.270000'), 'y': Decimal('643.060000'),
                                                           'w': Decimal('361.860000'), 'r': Decimal('539.130000'),
                                                           'h': Decimal('15.590000')}, 'text': '832850'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('626.500000'), 'w': Decimal('120.379000'), 'r': Decimal('176.408000'),
     'h': Decimal('16.070000')}, 'text': '法定代表人'}, {'pos': {'x': Decimal('177.270000'), 'y': Decimal('626.500000'),
                                                            'w': Decimal('361.860000'), 'r': Decimal('539.130000'),
                                                            'h': Decimal('16.070000')}, 'text': '张国义'}]]},
 {'el_type': 'p', 'text': '二、联系方式', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('574.390000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '公司指定信息披露平台的网址www.neeq.com.cn', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('610.300000'),
                                                                                             'w': Decimal('120.379000'),
                                                                                             'r': Decimal('176.408000'),
                                                                                             'h': Decimal('15.590000')},
                                                                                     'text': '办公地址'}, {'pos': {
     'x': Decimal('177.270000'), 'y': Decimal('610.300000'), 'w': Decimal('361.860000'), 'r': Decimal('539.130000'),
     'h': Decimal('15.590000')}, 'text': '昆明呈贡新城国家高新技术产业开发区'}], [{'pos': {'x': Decimal('56.029000'),
                                                                          'y': Decimal('546.910000'),
                                                                          'w': Decimal('177.169000'),
                                                                          'r': Decimal('233.198000'),
                                                                          'h': Decimal('15.600000')}, 'text': '董事会秘书'},
                                                                 {'pos': {'x': Decimal('234.050000'),
                                                                          'y': Decimal('546.910000'),
                                                                          'w': Decimal('305.090000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('15.600000')}, 'text': '李超'}], [{
     'pos': {
         'x': Decimal(
             '56.029000'),
         'y': Decimal(
             '515.230000'),
         'w': Decimal(
             '177.169000'),
         'r': Decimal(
             '233.198000'),
         'h': Decimal(
             '31.200000')},
     'text': '是否具备全国股转系统董事会秘书任职资格'},
                                                                                       {
                                                                                           'pos': {
                                                                                               'x': Decimal(
                                                                                                   '234.050000'),
                                                                                               'y': Decimal(
                                                                                                   '515.230000'),
                                                                                               'w': Decimal(
                                                                                                   '305.090000'),
                                                                                               'r': Decimal(
                                                                                                   '539.140000'),
                                                                                               'h': Decimal(
                                                                                                   '31.200000')},
                                                                                           'text': '是'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('499.150000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.600000')},
                                                                                     'text': '电话'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('499.150000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.600000')},
                                                                                        'text': '0871-67433888'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('483.070000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.600000')},
                                                                                     'text': '传真'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('483.070000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.600000')},
                                                                                        'text': '0871-67324178'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('466.870000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.600000')},
                                                                                     'text': '电子邮箱'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('466.870000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.600000')},
                                                                                        'text': 'lichao@yndzdj.com'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('450.790000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.600000')},
                                                                                     'text': '公司网址'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('450.790000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.600000')},
                                                                                        'text': 'www.yndzdj.com'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('434.710000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.600000')},
                                                                                     'text': '联系地址及邮政编码'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('434.710000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.600000')},
                                                                                        'text': '昆明呈贡新城国家高新技术产业开发区650503'}],
                                                                                   [{'pos': {'x': Decimal('56.029000'),
                                                                                             'y': Decimal('418.610000'),
                                                                                             'w': Decimal('177.169000'),
                                                                                             'r': Decimal('233.198000'),
                                                                                             'h': Decimal('15.620000')},
                                                                                     'text': '公司指定信息披露平台的网址'}, {'pos': {
                                                                                       'x': Decimal('234.050000'),
                                                                                       'y': Decimal('418.610000'),
                                                                                       'w': Decimal('305.090000'),
                                                                                       'r': Decimal('539.140000'),
                                                                                       'h': Decimal('15.620000')},
                                                                                        'text': 'www.neeq.com.cn'}]]},
 {'el_type': 'p', 'text': '三、企业信息', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('366.650000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '控股股东张国义', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                        'y': Decimal('402.530000'),
                                                                        'w': Decimal('177.169000'),
                                                                        'r': Decimal('233.198000'),
                                                                        'h': Decimal('15.590000')},
                                                                'text': '公司年度报告备置地'}, {
                                                                   'pos': {'x': Decimal('234.050000'),
                                                                           'y': Decimal('402.530000'),
                                                                           'w': Decimal('305.090000'),
                                                                           'r': Decimal('539.140000'),
                                                                           'h': Decimal('15.590000')},
                                                                   'text': '董事会办公室'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('339.050000'), 'w': Decimal('177.169000'), 'r': Decimal('233.198000'),
     'h': Decimal('15.590000')}, 'text': '股票公开转让场所'}, {'pos': {'x': Decimal('234.050000'), 'y': Decimal('339.050000'),
                                                               'w': Decimal('305.090000'), 'r': Decimal('539.140000'),
                                                               'h': Decimal('15.590000')}, 'text': '全国中小企业股份转让系统'}], [{
     'pos': {
         'x': Decimal(
             '56.029000'),
         'y': Decimal(
             '322.970000'),
         'w': Decimal(
             '177.169000'),
         'r': Decimal(
             '233.198000'),
         'h': Decimal(
             '15.590000')},
     'text': '成立时间'},
                                                                  {
                                                                      'pos': {
                                                                          'x': Decimal(
                                                                              '234.050000'),
                                                                          'y': Decimal(
                                                                              '322.970000'),
                                                                          'w': Decimal(
                                                                              '305.090000'),
                                                                          'r': Decimal(
                                                                              '539.140000'),
                                                                          'h': Decimal(
                                                                              '15.590000')},
                                                                      'text': '2008年4月8日'}],
                                                              [{'pos': {'x': Decimal('56.029000'),
                                                                        'y': Decimal('306.890000'),
                                                                        'w': Decimal('177.169000'),
                                                                        'r': Decimal('233.198000'),
                                                                        'h': Decimal('15.590000')}, 'text': '挂牌时间'}, {
                                                                   'pos': {'x': Decimal('234.050000'),
                                                                           'y': Decimal('306.890000'),
                                                                           'w': Decimal('305.090000'),
                                                                           'r': Decimal('539.140000'),
                                                                           'h': Decimal('15.590000')},
                                                                   'text': '2015年7月22日'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('290.810000'), 'w': Decimal('177.169000'), 'r': Decimal('233.198000'),
         'h': Decimal('15.590000')}, 'text': '分层情况'}, {'pos': {'x': Decimal('234.050000'), 'y': Decimal('290.810000'),
                                                               'w': Decimal('305.090000'), 'r': Decimal('539.140000'),
                                                               'h': Decimal('15.590000')}, 'text': '创新层'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('259.110000'), 'w': Decimal('177.169000'), 'r': Decimal('233.198000'),
         'h': Decimal('31.214000')}, 'text': '行业（挂牌公司管理型行业分类）'}, {'pos': {'x': Decimal('234.050000'),
                                                                          'y': Decimal('259.110000'),
                                                                          'w': Decimal('305.090000'),
                                                                          'r': Decimal('539.140000'),
                                                                          'h': Decimal('31.214000')},
                                                                  'text': 'C制造业-32有色金属冶炼和压延加工业-321常用有色金属冶炼-3219其他常用有色金属冶炼'}],
                                                              [{'pos': {'x': Decimal('56.029000'),
                                                                        'y': Decimal('243.030000'),
                                                                        'w': Decimal('177.169000'),
                                                                        'r': Decimal('233.198000'),
                                                                        'h': Decimal('15.590000')},
                                                                'text': '主要产品与服务项目'}, {
                                                                   'pos': {'x': Decimal('234.050000'),
                                                                           'y': Decimal('243.030000'),
                                                                           'w': Decimal('305.090000'),
                                                                           'r': Decimal('539.140000'),
                                                                           'h': Decimal('15.590000')},
                                                                   'text': '湿法冶金用阳极板、阴极板及极板技术整套服务'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('226.830000'), 'w': Decimal('177.169000'), 'r': Decimal('233.198000'),
         'h': Decimal('15.590000')}, 'text': '普通股股票转让方式'}, {'pos': {'x': Decimal('234.050000'),
                                                                    'y': Decimal('226.830000'),
                                                                    'w': Decimal('305.090000'),
                                                                    'r': Decimal('539.140000'),
                                                                    'h': Decimal('15.590000')}, 'text': '做市转让'}], [{
         'pos': {
             'x': Decimal(
                 '56.029000'),
             'y': Decimal(
                 '210.150000'),
             'w': Decimal(
                 '177.169000'),
             'r': Decimal(
                 '233.198000'),
             'h': Decimal(
                 '16.190000')},
         'text': '普通股总股本（股）'},
                                                                  {
                                                                      'pos': {
                                                                          'x': Decimal(
                                                                              '234.050000'),
                                                                          'y': Decimal(
                                                                              '210.150000'),
                                                                          'w': Decimal(
                                                                              '305.090000'),
                                                                          'r': Decimal(
                                                                              '539.140000'),
                                                                          'h': Decimal(
                                                                              '16.190000')},
                                                                      'text': '50,850,000'}],
                                                              [{'pos': {'x': Decimal('56.029000'),
                                                                        'y': Decimal('193.350000'),
                                                                        'w': Decimal('177.169000'),
                                                                        'r': Decimal('233.198000'),
                                                                        'h': Decimal('16.310000')},
                                                                'text': '优先股总股本（股）'}, {
                                                                   'pos': {'x': Decimal('234.050000'),
                                                                           'y': Decimal('193.350000'),
                                                                           'w': Decimal('305.090000'),
                                                                           'r': Decimal('539.140000'),
                                                                           'h': Decimal('16.310000')}, 'text': '0'}], [{
         'pos': {
             'x': Decimal(
                 '56.029000'),
             'y': Decimal(
                 '176.670000'),
             'w': Decimal(
                 '177.169000'),
             'r': Decimal(
                 '233.198000'),
             'h': Decimal(
                 '16.190000')},
         'text': '做市商数量'},
                                                                  {
                                                                      'pos': {
                                                                          'x': Decimal(
                                                                              '234.050000'),
                                                                          'y': Decimal(
                                                                              '176.670000'),
                                                                          'w': Decimal(
                                                                              '305.090000'),
                                                                          'r': Decimal(
                                                                              '539.140000'),
                                                                          'h': Decimal(
                                                                              '16.190000')},
                                                                      'text': '2'}],
                                                              [{'pos': {'x': Decimal('56.029000'),
                                                                        'y': Decimal('160.590000'),
                                                                        'w': Decimal('177.169000'),
                                                                        'r': Decimal('233.198000'),
                                                                        'h': Decimal('15.590000')}, 'text': '控股股东'}, {
                                                                   'pos': {'x': Decimal('234.050000'),
                                                                           'y': Decimal('160.590000'),
                                                                           'w': Decimal('305.090000'),
                                                                           'r': Decimal('539.140000'),
                                                                           'h': Decimal('15.590000')},
                                                                   'text': '张国义'}]]},
 {'el_type': 'p', 'text': '四、注册情况', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('108.500000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '注册资本50,850,000否', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                'y': Decimal('144.390000'),
                                                                                'w': Decimal('177.169000'),
                                                                                'r': Decimal('233.198000'),
                                                                                'h': Decimal('15.590000')},
                                                                        'text': '实际控制人及其一致行动人'}, {
                                                                           'pos': {'x': Decimal('234.050000'),
                                                                                   'y': Decimal('144.390000'),
                                                                                   'w': Decimal('305.090000'),
                                                                                   'r': Decimal('539.140000'),
                                                                                   'h': Decimal('15.590000')},
                                                                           'text': '张国义'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('753.820000'), 'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
     'h': Decimal('15.620000')}, 'text': '实际控制人及其一致行动人'}, {'pos': {'x': Decimal('231.050000'),
                                                                   'y': Decimal('753.820000'),
                                                                   'w': Decimal('164.540000'),
                                                                   'r': Decimal('395.590000'),
                                                                   'h': Decimal('15.620000')}, 'text': '实际控制人及其一致行动人'},
                                                                          {'pos': {'x': Decimal(
                                                                              '397.750000'),
                                                                              'y': Decimal(
                                                                                  '753.820000'),
                                                                              'w': Decimal(
                                                                                  '142.210000'),
                                                                              'r': Decimal(
                                                                                  '539.960000'),
                                                                              'h': Decimal(
                                                                                  '15.620000')},
                                                                              'text': '实际控制人及其一致行动人'}, {
         'pos': {'x': Decimal(
             '56.029000'),
             'y': Decimal(
                 '77.760000'),
             'w': Decimal(
                 '175.009000'),
             'r': Decimal(
                 '231.038000'),
             'h': Decimal(
                 '18.839000')},
         'text': '项目'}, {
         'pos': {'x': Decimal(
             '231.050000'),
             'y': Decimal(
                 '77.760000'),
             'w': Decimal(
                 '164.540000'),
             'r': Decimal(
                 '395.590000'),
             'h': Decimal(
                 '18.839000')},
         'text': '内容'}, {
         'pos': {'x': Decimal(
             '397.750000'),
             'y': Decimal(
                 '77.760000'),
             'w': Decimal(
                 '142.210000'),
             'r': Decimal(
                 '539.960000'),
             'h': Decimal(
                 '18.839000')},
         'text': '报告期内是否变更'}], [
                                                                          {'pos': {'x': Decimal('56.029000'),
                                                                                   'y': Decimal('530.000000'),
                                                                                   'w': Decimal('483.500000'),
                                                                                   'r': Decimal('539.529000'),
                                                                                   'h': Decimal('257.000000')},
                                                                           'text': ''}, {
         'pos': {'x': Decimal('56.029000'),
                 'y': Decimal('753.820000'),
                 'w': Decimal('175.009000'),
                 'r': Decimal('231.038000'),
                 'h': Decimal('15.620000')},
         'text': '统一社会信用代码'}, {
         'pos': {'x': Decimal('231.050000'),
                 'y': Decimal('753.820000'),
                 'w': Decimal('164.540000'),
                 'r': Decimal('395.590000'),
                 'h': Decimal('15.620000')},
         'text': '91530100673606509Y'}, {
         'pos': {'x': Decimal('397.750000'),
                 'y': Decimal('753.820000'),
                 'w': Decimal('142.210000'),
                 'r': Decimal('539.960000'),
                 'h': Decimal('15.620000')},
         'text': '否'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('753.820000'), 'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
     'h': Decimal('15.620000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('753.820000'),
                                                       'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
                                                       'h': Decimal('15.620000')}, 'text': '统一社会信用代码'}, {'pos': {
     'x': Decimal('231.050000'), 'y': Decimal('753.820000'), 'w': Decimal('164.540000'), 'r': Decimal('395.590000'),
     'h': Decimal('15.620000')}, 'text': ''}, {'pos': {'x': Decimal('397.750000'), 'y': Decimal('753.820000'),
                                                       'w': Decimal('142.210000'), 'r': Decimal('539.960000'),
                                                       'h': Decimal('15.620000')}, 'text': ''}, {'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('706.540000'), 'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
     'h': Decimal('46.790000')}, 'text': '注册地址'}, {'pos': {'x': Decimal('231.050000'), 'y': Decimal('706.540000'),
                                                           'w': Decimal('164.540000'), 'r': Decimal('395.590000'),
                                                           'h': Decimal('46.790000')},
                                                   'text': '云南省昆明市高新技术开发区新城高新技术产业基地B-5-10-1号地块'}, {'pos': {
     'x': Decimal('397.750000'), 'y': Decimal('706.540000'), 'w': Decimal('142.210000'), 'r': Decimal('539.960000'),
     'h': Decimal('46.790000')}, 'text': '否'}], [{'pos': {'x': Decimal('56.029000'), 'y': Decimal('690.460000'),
                                                          'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
                                                          'h': Decimal('15.590000')}, 'text': '注册资本'}, {
                                                     'pos': {'x': Decimal('56.029000'), 'y': Decimal('706.540000'),
                                                             'w': Decimal('175.009000'), 'r': Decimal('231.038000'),
                                                             'h': Decimal('46.790000')}, 'text': '注册地址'}, {
                                                     'pos': {'x': Decimal('231.050000'), 'y': Decimal('690.460000'),
                                                             'w': Decimal('164.540000'), 'r': Decimal('395.590000'),
                                                             'h': Decimal('15.590000')}, 'text': '50,850,000'}, {
                                                     'pos': {'x': Decimal('397.750000'), 'y': Decimal('690.460000'),
                                                             'w': Decimal('142.210000'), 'r': Decimal('539.960000'),
                                                             'h': Decimal('15.590000')}, 'text': '否'}]]},
 {'el_type': 'p', 'text': '五、中介机构', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('638.380000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'table', 'table_name': '签字注册会计师姓名孙立倩、高峰', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                'y': Decimal('674.260000'),
                                                                                'w': Decimal('482.730000'),
                                                                                'r': Decimal('538.759000'),
                                                                                'h': Decimal('15.590000')}, 'text': ''},
                                                                       {'pos': {'x': Decimal('56.029000'),
                                                                                'y': Decimal('610.900000'),
                                                                                'w': Decimal('184.249000'),
                                                                                'r': Decimal('240.278000'),
                                                                                'h': Decimal('15.590000')},
                                                                        'text': '主办券商'}, {
                                                                           'pos': {'x': Decimal('240.170000'),
                                                                                   'y': Decimal('610.900000'),
                                                                                   'w': Decimal('298.010000'),
                                                                                   'r': Decimal('538.180000'),
                                                                                   'h': Decimal('15.590000')},
                                                                           'text': '东北证券'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('610.900000'), 'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
     'h': Decimal('15.590000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('610.900000'),
                                                       'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
                                                       'h': Decimal('15.590000')}, 'text': '主办券商'}, {'pos': {
     'x': Decimal('240.170000'), 'y': Decimal('610.900000'), 'w': Decimal('298.010000'), 'r': Decimal('538.180000'),
     'h': Decimal('15.590000')}, 'text': ''}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('594.790000'),
                                                       'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
                                                       'h': Decimal('15.615000')}, 'text': '主办券商办公地址'}, {'pos': {
     'x': Decimal('240.170000'), 'y': Decimal('594.790000'), 'w': Decimal('298.010000'), 'r': Decimal('538.180000'),
     'h': Decimal('15.615000')}, 'text': '北京市西城区三里河东路5号中商大厦4层'}], [{'pos': {'x': Decimal('56.029000'),
                                                                            'y': Decimal('578.710000'),
                                                                            'w': Decimal('184.249000'),
                                                                            'r': Decimal('240.278000'),
                                                                            'h': Decimal('15.600000')},
                                                                    'text': '报告期内主办券商是否发生变化'}, {
                                                                       'pos': {'x': Decimal('56.029000'),
                                                                               'y': Decimal('594.790000'),
                                                                               'w': Decimal('184.249000'),
                                                                               'r': Decimal('240.278000'),
                                                                               'h': Decimal('15.615000')},
                                                                       'text': '主办券商办公地址'}, {
                                                                       'pos': {'x': Decimal('240.170000'),
                                                                               'y': Decimal('578.710000'),
                                                                               'w': Decimal('298.010000'),
                                                                               'r': Decimal('538.180000'),
                                                                               'h': Decimal('15.600000')},
                                                                       'text': '否'}], [{'pos': {
     'x': Decimal('56.029000'), 'y': Decimal('562.630000'), 'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
     'h': Decimal('15.600000')}, 'text': '会计师事务所'}, {'pos': {'x': Decimal('56.029000'), 'y': Decimal('578.710000'),
                                                             'w': Decimal('184.249000'), 'r': Decimal('240.278000'),
                                                             'h': Decimal('15.600000')}, 'text': '报告期内主办券商是否发生变化'}, {
     'pos': {'x': Decimal(
         '240.170000'),
         'y': Decimal(
             '562.630000'),
         'w': Decimal(
             '298.010000'),
         'r': Decimal(
             '538.180000'),
         'h': Decimal(
             '15.600000')},
     'text': '众华会计师事务所(特殊普通合伙)'}],
                                                                      [{'pos': {'x': Decimal('56.029000'),
                                                                                'y': Decimal('546.430000'),
                                                                                'w': Decimal('184.249000'),
                                                                                'r': Decimal('240.278000'),
                                                                                'h': Decimal('15.600000')},
                                                                        'text': '签字注册会计师姓名'}, {
                                                                           'pos': {'x': Decimal('56.029000'),
                                                                                   'y': Decimal('562.630000'),
                                                                                   'w': Decimal('184.249000'),
                                                                                   'r': Decimal('240.278000'),
                                                                                   'h': Decimal('15.600000')},
                                                                           'text': '会计师事务所'}, {
                                                                           'pos': {'x': Decimal('240.170000'),
                                                                                   'y': Decimal('546.430000'),
                                                                                   'w': Decimal('298.010000'),
                                                                                   'r': Decimal('538.180000'),
                                                                                   'h': Decimal('15.600000')},
                                                                           'text': '孙立倩、高峰'}]]},
 {'el_type': 'p', 'text': '六、自愿披露', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('45.703125'), 'y': Decimal('494.470000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '□适用√不适用', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('471.430000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('456.070000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '七、报告期后更新情况', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('432.050000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '□适用√不适用', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.145000'), 'y': Decimal('409.010000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('393.650000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('378.050000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('35.806641'), 'y': Decimal('51.960000'),
                 'fs': Decimal('36.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '第三节会计数据和财务指标摘要', 'table_name': '',
  'style_dict': {'x': Decimal('188.900000'), 'h': Decimal('59.625000'), 'y': Decimal('743.260000'),
                 'fs': Decimal('56.160000'), 'w': Decimal('0.000000'), 'r': Decimal('188.900000')}},
 {'el_type': 'p', 'text': '一、盈利能力', 'table_name': '',
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('39.937500'), 'y': Decimal('712.900000'),
                 'fs': Decimal('48.000000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000')}},
 {'el_type': 'p', 'text': '单位：元', 'table_name': '',
  'style_dict': {'x': Decimal('491.980000'), 'h': Decimal('42.013125'), 'y': Decimal('689.860000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('491.980000')}},
 {'el_type': 'table', 'text': '', 'table_name': '盈利能力', 'table_data': [[{'pos': {'x': Decimal('56.029000'),
                                                                                 'y': Decimal('669.820000'),
                                                                                 'w': Decimal('181.249000'),
                                                                                 'r': Decimal('237.278000'),
                                                                                 'h': Decimal('15.590000')},
                                                                         'text': '会计师事务所办公地址'}, {
                                                                            'pos': {'x': Decimal('238.130000'),
                                                                                    'y': Decimal('669.820000'),
                                                                                    'w': Decimal('112.940000'),
                                                                                    'r': Decimal('351.070000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '会计师事务所办公地址'}, {
                                                                            'pos': {'x': Decimal('351.680000'),
                                                                                    'y': Decimal('669.820000'),
                                                                                    'w': Decimal('110.050000'),
                                                                                    'r': Decimal('461.730000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '会计师事务所办公地址'}, {
                                                                            'pos': {'x': Decimal('462.340000'),
                                                                                    'y': Decimal('669.820000'),
                                                                                    'w': Decimal('76.790000'),
                                                                                    'r': Decimal('539.130000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '会计师事务所办公地址'}, {
                                                                            'pos': {'x': Decimal('240.170000'),
                                                                                    'y': Decimal('530.350000'),
                                                                                    'w': Decimal('298.010000'),
                                                                                    'r': Decimal('538.180000'),
                                                                                    'h': Decimal('15.600000')},
                                                                            'text': '上海市黄浦区中山南路100号金外滩国际广场6楼'}], [{
     'pos': {
         'x': Decimal(
             '56.029000'),
         'y': Decimal(
             '669.820000'),
         'w': Decimal(
             '181.249000'),
         'r': Decimal(
             '237.278000'),
         'h': Decimal(
             '15.590000')},
     'text': ''},
                                                                           {
                                                                               'pos': {
                                                                                   'x': Decimal(
                                                                                       '238.130000'),
                                                                                   'y': Decimal(
                                                                                       '669.820000'),
                                                                                   'w': Decimal(
                                                                                       '112.940000'),
                                                                                   'r': Decimal(
                                                                                       '351.070000'),
                                                                                   'h': Decimal(
                                                                                       '15.590000')},
                                                                               'text': '本期'},
                                                                           {
                                                                               'pos': {
                                                                                   'x': Decimal(
                                                                                       '351.680000'),
                                                                                   'y': Decimal(
                                                                                       '669.820000'),
                                                                                   'w': Decimal(
                                                                                       '110.050000'),
                                                                                   'r': Decimal(
                                                                                       '461.730000'),
                                                                                   'h': Decimal(
                                                                                       '15.590000')},
                                                                               'text': '上年同期'},
                                                                           {
                                                                               'pos': {
                                                                                   'x': Decimal(
                                                                                       '462.340000'),
                                                                                   'y': Decimal(
                                                                                       '669.820000'),
                                                                                   'w': Decimal(
                                                                                       '76.790000'),
                                                                                   'r': Decimal(
                                                                                       '539.130000'),
                                                                                   'h': Decimal(
                                                                                       '15.590000')},
                                                                               'text': '增减比例%'}],
                                                                       [{'pos': {'x': Decimal('56.029000'),
                                                                                 'y': Decimal('653.740000'),
                                                                                 'w': Decimal('181.249000'),
                                                                                 'r': Decimal('237.278000'),
                                                                                 'h': Decimal('15.590000')},
                                                                         'text': '营业收入'}, {
                                                                            'pos': {'x': Decimal('238.130000'),
                                                                                    'y': Decimal('653.740000'),
                                                                                    'w': Decimal('112.940000'),
                                                                                    'r': Decimal('351.070000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '231,321,934.28'}, {
                                                                            'pos': {'x': Decimal('351.680000'),
                                                                                    'y': Decimal('653.740000'),
                                                                                    'w': Decimal('110.050000'),
                                                                                    'r': Decimal('461.730000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '219,172,374.28'}, {
                                                                            'pos': {'x': Decimal('462.340000'),
                                                                                    'y': Decimal('653.740000'),
                                                                                    'w': Decimal('76.790000'),
                                                                                    'r': Decimal('539.130000'),
                                                                                    'h': Decimal('15.590000')},
                                                                            'text': '5.54%'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('637.660000'), 'w': Decimal('181.249000'), 'r': Decimal('237.278000'),
         'h': Decimal('15.590000')}, 'text': '毛利率%'}, {'pos': {'x': Decimal('238.130000'), 'y': Decimal('637.660000'),
                                                               'w': Decimal('112.940000'), 'r': Decimal('351.070000'),
                                                               'h': Decimal('15.590000')}, 'text': '12.79%'}, {'pos': {
         'x': Decimal('351.680000'), 'y': Decimal('637.660000'), 'w': Decimal('110.050000'), 'r': Decimal('461.730000'),
         'h': Decimal('15.590000')}, 'text': '8.56%'}, {'pos': {'x': Decimal('462.340000'), 'y': Decimal('637.660000'),
                                                                'w': Decimal('76.790000'), 'r': Decimal('539.130000'),
                                                                'h': Decimal('15.590000')}, 'text': '-'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('621.460000'), 'w': Decimal('181.249000'), 'r': Decimal('237.278000'),
         'h': Decimal('15.590000')}, 'text': '归属于挂牌公司股东的净利润'}, {'pos': {'x': Decimal('238.130000'),
                                                                        'y': Decimal('621.460000'),
                                                                        'w': Decimal('112.940000'),
                                                                        'r': Decimal('351.070000'),
                                                                        'h': Decimal('15.590000')},
                                                                'text': '7,283,505.67'}, {'pos': {
         'x': Decimal('351.680000'), 'y': Decimal('621.460000'), 'w': Decimal('110.050000'), 'r': Decimal('461.730000'),
         'h': Decimal('15.590000')}, 'text': '539,679.75'}, {'pos': {'x': Decimal('462.340000'),
                                                                     'y': Decimal('621.460000'),
                                                                     'w': Decimal('76.790000'),
                                                                     'r': Decimal('539.130000'),
                                                                     'h': Decimal('15.590000')}, 'text': '1,249.60%'}],
                                                                       [{'pos': {'x': Decimal('56.029000'),
                                                                                 'y': Decimal('589.750000'),
                                                                                 'w': Decimal('181.249000'),
                                                                                 'r': Decimal('237.278000'),
                                                                                 'h': Decimal('31.215000')},
                                                                         'text': '归属于挂牌公司股东的扣除非经常性损益后的净利润'}, {
                                                                            'pos': {'x': Decimal('238.130000'),
                                                                                    'y': Decimal('589.750000'),
                                                                                    'w': Decimal('112.940000'),
                                                                                    'r': Decimal('351.070000'),
                                                                                    'h': Decimal('31.215000')},
                                                                            'text': '6,204,148.71'}, {
                                                                            'pos': {'x': Decimal('351.680000'),
                                                                                    'y': Decimal('589.750000'),
                                                                                    'w': Decimal('110.050000'),
                                                                                    'r': Decimal('461.730000'),
                                                                                    'h': Decimal('31.215000')},
                                                                            'text': '-210,843.59'}, {
                                                                            'pos': {'x': Decimal('462.340000'),
                                                                                    'y': Decimal('589.750000'),
                                                                                    'w': Decimal('76.790000'),
                                                                                    'r': Decimal('539.130000'),
                                                                                    'h': Decimal('31.215000')},
                                                                            'text': '3,042.54%'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('558.070000'), 'w': Decimal('181.249000'), 'r': Decimal('237.278000'),
         'h': Decimal('31.200000')}, 'text': '加权平均净资产收益率%（依据归属于挂牌公司股东的净利润计算）'}, {'pos': {'x': Decimal('238.130000'),
                                                                                         'y': Decimal('558.070000'),
                                                                                         'w': Decimal('112.940000'),
                                                                                         'r': Decimal('351.070000'),
                                                                                         'h': Decimal('31.200000')},
                                                                                 'text': '13.95%'}, {'pos': {
         'x': Decimal('351.680000'), 'y': Decimal('558.070000'), 'w': Decimal('110.050000'), 'r': Decimal('461.730000'),
         'h': Decimal('31.200000')}, 'text': '1.12%'}, {'pos': {'x': Decimal('462.340000'), 'y': Decimal('558.070000'),
                                                                'w': Decimal('76.790000'), 'r': Decimal('539.130000'),
                                                                'h': Decimal('31.200000')}, 'text': '-'}], [{'pos': {
         'x': Decimal('56.029000'), 'y': Decimal('510.790000'), 'w': Decimal('181.249000'), 'r': Decimal('237.278000'),
         'h': Decimal('46.800000')}, 'text': '加权平均净资产收益率%（归属于挂牌公司股东的扣除非经常性损益后的净利润计算）'}, {'pos': {
         'x': Decimal('238.130000'), 'y': Decimal('510.790000'), 'w': Decimal('112.940000'), 'r': Decimal('351.070000'),
         'h': Decimal('46.800000')}, 'text': '11.88%'}, {'pos': {'x': Decimal('351.680000'), 'y': Decimal('510.790000'),
                                                                 'w': Decimal('110.050000'), 'r': Decimal('461.730000'),
                                                                 'h': Decimal('46.800000')}, 'text': '-0.44%'}, {
         'pos': {
             'x': Decimal(
                 '462.340000'),
             'y': Decimal(
                 '510.790000'),
             'w': Decimal(
                 '76.790000'),
             'r': Decimal(
                 '539.130000'),
             'h': Decimal(
                 '46.800000')},
         'text': '-'}]],
  'style_dict': {'x': Decimal('61.560000'), 'h': Decimal('42.013125'), 'y': Decimal('482.830000'),
                 'fs': Decimal('42.240000'), 'w': Decimal('0.000000'), 'r': Decimal('61.560000'...
