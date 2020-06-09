#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from decimal import Decimal

table_list = [
    {'x0': Decimal('289.250'), 'x1': Decimal('310.370'), 'top': Decimal('176.469'), 'bottom': Decimal('187.029'),
     'upright': 1, 'text': '期初', 'id': '33024ba7-a642-11ea-9aae-f48e3877e5fc'},
    {'x0': Decimal('469.420'), 'x1': Decimal('490.540'), 'top': Decimal('176.469'), 'bottom': Decimal('187.029'),
     'upright': 1, 'text': '期末', 'id': '33024ba8-a642-11ea-b043-f48e3877e5fc'},
    {'x0': Decimal('127.340'), 'x1': Decimal('169.580'), 'top': Decimal('184.509'), 'bottom': Decimal('195.069'),
     'upright': 1, 'text': '股份性质', 'id': '33024ba9-a642-11ea-88d9-f48e3877e5fc'},
    {'x0': Decimal('368.830'), 'x1': Decimal('411.070'), 'top': Decimal('184.509'), 'bottom': Decimal('195.069'),
     'upright': 1, 'text': '本期变动', 'id': '330272b4-a642-11ea-8cc6-f48e3877e5fc'},
    {'x0': Decimal('260.570'), 'x1': Decimal('281.690'), 'top': Decimal('192.549'), 'bottom': Decimal('203.109'),
     'upright': 1, 'text': '数量', 'id': '330272b5-a642-11ea-96f9-f48e3877e5fc'},
    {'x0': Decimal('316.010'), 'x1': Decimal('344.848'), 'top': Decimal('192.549'), 'bottom': Decimal('204.260'),
     'upright': 1, 'text': '比例%', 'id': '330272b6-a642-11ea-8611-f48e3877e5fc'},
    {'x0': Decimal('441.550'), 'x1': Decimal('462.670'), 'top': Decimal('192.549'), 'bottom': Decimal('203.109'),
     'upright': 1, 'text': '数量', 'id': '330272b7-a642-11ea-805c-f48e3877e5fc'},
    {'x0': Decimal('497.140'), 'x1': Decimal('525.958'), 'top': Decimal('192.549'), 'bottom': Decimal('204.260'),
     'upright': 1, 'text': '比例%', 'id': '330272b8-a642-11ea-a6a5-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('184.344'), 'top': Decimal('208.629'), 'bottom': Decimal('219.189'),
     'upright': 1, 'text': '无限售股份总数', 'id': '330299c2-a642-11ea-8beb-f48e3877e5fc'},
    {'x0': Decimal('248.570'), 'x1': Decimal('296.365'), 'top': Decimal('209.540'), 'bottom': Decimal('220.100'),
     'upright': 1, 'text': '20,213,250', 'id': '330299c3-a642-11ea-b937-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('209.540'), 'bottom': Decimal('220.100'),
     'upright': 1, 'text': '39.75%', 'id': '330299c4-a642-11ea-bd7c-f48e3877e5fc'},
    {'x0': Decimal('382.870'), 'x1': Decimal('415.330'), 'top': Decimal('209.540'), 'bottom': Decimal('220.100'),
     'upright': 1, 'text': '-50,250', 'id': '330299c5-a642-11ea-b4d1-f48e3877e5fc'},
    {'x0': Decimal('430.390'), 'x1': Decimal('478.185'), 'top': Decimal('209.540'), 'bottom': Decimal('220.100'),
     'upright': 1, 'text': '20,163,000', 'id': '330299c6-a642-11ea-8c42-f48e3877e5fc'},
    {'x0': Decimal('502.540'), 'x1': Decimal('534.051'), 'top': Decimal('209.540'), 'bottom': Decimal('220.100'),
     'upright': 1, 'text': '39.65%', 'id': '330299c7-a642-11ea-a671-f48e3877e5fc'},
    {'x0': Decimal('64.944'), 'x1': Decimal('96.624'), 'top': Decimal('225.069'), 'bottom': Decimal('235.629'),
     'upright': 1, 'text': '无限售', 'id': '330299c8-a642-11ea-ab8a-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('235.232'), 'top': Decimal('224.829'), 'bottom': Decimal('235.389'),
     'upright': 1, 'text': '其中：控股股东、实际控制', 'id': '3302c0d2-a642-11ea-b675-f48e3877e5fc'},
    {'x0': Decimal('253.850'), 'x1': Decimal('296.365'), 'top': Decimal('225.740'), 'bottom': Decimal('236.300'),
     'upright': 1, 'text': '8,706,250', 'id': '3302c0d3-a642-11ea-ac8c-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('225.740'), 'bottom': Decimal('236.300'),
     'upright': 1, 'text': '17.12%', 'id': '3302c0d4-a642-11ea-a41e-f48e3877e5fc'},
    {'x0': Decimal('372.790'), 'x1': Decimal('415.305'), 'top': Decimal('225.740'), 'bottom': Decimal('236.300'),
     'upright': 1, 'text': '1,544,750', 'id': '3302c0d5-a642-11ea-95c6-f48e3877e5fc'},
    {'x0': Decimal('430.390'), 'x1': Decimal('478.185'), 'top': Decimal('225.740'), 'bottom': Decimal('236.300'),
     'upright': 1, 'text': '10,251,000', 'id': '3302c0d6-a642-11ea-b5bb-f48e3877e5fc'},
    {'x0': Decimal('502.540'), 'x1': Decimal('534.051'), 'top': Decimal('225.740'), 'bottom': Decimal('236.300'),
     'upright': 1, 'text': '20.16%', 'id': '3302c0d7-a642-11ea-863a-f48e3877e5fc'},
    {'x0': Decimal('64.944'), 'x1': Decimal('96.624'), 'top': Decimal('240.699'), 'bottom': Decimal('251.259'),
     'upright': 1, 'text': '条件股', 'id': '3302c0d8-a642-11ea-93ad-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('121.220'), 'top': Decimal('240.459'), 'bottom': Decimal('251.019'),
     'upright': 1, 'text': '人', 'id': '3302e7e4-a642-11ea-9842-f48e3877e5fc'},
    {'x0': Decimal('75.504'), 'x1': Decimal('86.064'), 'top': Decimal('256.299'), 'bottom': Decimal('266.859'),
     'upright': 1, 'text': '份', 'id': '3302e7e5-a642-11ea-a92f-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('194.792'), 'top': Decimal('256.539'), 'bottom': Decimal('267.099'),
     'upright': 1, 'text': '董事、监事、高管', 'id': '3302e7e6-a642-11ea-9c4d-f48e3877e5fc'},
    {'x0': Decimal('253.850'), 'x1': Decimal('296.365'), 'top': Decimal('257.450'), 'bottom': Decimal('268.010'),
     'upright': 1, 'text': '1,506,000', 'id': '3302e7e7-a642-11ea-beff-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('257.450'), 'bottom': Decimal('268.010'),
     'upright': 1, 'text': '20.08%', 'id': '3302e7e8-a642-11ea-9da5-f48e3877e5fc'},
    {'x0': Decimal('377.470'), 'x1': Decimal('415.305'), 'top': Decimal('257.450'), 'bottom': Decimal('268.010'),
     'upright': 1, 'text': '-999,000', 'id': '3302e7e9-a642-11ea-b172-f48e3877e5fc'},
    {'x0': Decimal('443.590'), 'x1': Decimal('478.185'), 'top': Decimal('257.450'), 'bottom': Decimal('268.010'),
     'upright': 1, 'text': '507,000', 'id': '3302e7ea-a642-11ea-aef2-f48e3877e5fc'},
    {'x0': Decimal('521.140'), 'x1': Decimal('534.090'), 'top': Decimal('257.450'), 'bottom': Decimal('268.010'),
     'upright': 1, 'text': '1%', 'id': '33030ef4-a642-11ea-b47c-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('152.784'), 'top': Decimal('272.619'), 'bottom': Decimal('283.179'),
     'upright': 1, 'text': '核心员工', 'id': '33030ef5-a642-11ea-b5bb-f48e3877e5fc'},
    {'x0': Decimal('291.050'), 'x1': Decimal('296.404'), 'top': Decimal('273.530'), 'bottom': Decimal('284.090'),
     'upright': 1, 'text': '0', 'id': '33030ef6-a642-11ea-bdf3-f48e3877e5fc'},
    {'x0': Decimal('340.870'), 'x1': Decimal('353.820'), 'top': Decimal('273.530'), 'bottom': Decimal('284.090'),
     'upright': 1, 'text': '0%', 'id': '33030ef7-a642-11ea-99cd-f48e3877e5fc'},
    {'x0': Decimal('409.990'), 'x1': Decimal('415.344'), 'top': Decimal('273.530'), 'bottom': Decimal('284.090'),
     'upright': 1, 'text': '0', 'id': '33030ef8-a642-11ea-b626-f48e3877e5fc'},
    {'x0': Decimal('472.900'), 'x1': Decimal('478.254'), 'top': Decimal('273.530'), 'bottom': Decimal('284.090'),
     'upright': 1, 'text': '0', 'id': '33030ef9-a642-11ea-9bb7-f48e3877e5fc'},
    {'x0': Decimal('521.140'), 'x1': Decimal('534.090'), 'top': Decimal('273.530'), 'bottom': Decimal('284.090'),
     'upright': 1, 'text': '0%', 'id': '33030efa-a642-11ea-a630-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('184.344'), 'top': Decimal('288.699'), 'bottom': Decimal('299.259'),
     'upright': 1, 'text': '有限售股份总数', 'id': '33033606-a642-11ea-b4b4-f48e3877e5fc'},
    {'x0': Decimal('248.570'), 'x1': Decimal('296.365'), 'top': Decimal('289.610'), 'bottom': Decimal('300.170'),
     'upright': 1, 'text': '30,636,750', 'id': '33033607-a642-11ea-8b91-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('289.610'), 'bottom': Decimal('300.170'),
     'upright': 1, 'text': '60.25%', 'id': '33033608-a642-11ea-9103-f48e3877e5fc'},
    {'x0': Decimal('385.990'), 'x1': Decimal('415.305'), 'top': Decimal('289.610'), 'bottom': Decimal('300.170'),
     'upright': 1, 'text': '50,250', 'id': '33033609-a642-11ea-9e0f-f48e3877e5fc'},
    {'x0': Decimal('430.390'), 'x1': Decimal('478.185'), 'top': Decimal('289.610'), 'bottom': Decimal('300.170'),
     'upright': 1, 'text': '30,687,000', 'id': '3303360a-a642-11ea-8240-f48e3877e5fc'},
    {'x0': Decimal('502.540'), 'x1': Decimal('534.051'), 'top': Decimal('289.610'), 'bottom': Decimal('300.170'),
     'upright': 1, 'text': '60.35%', 'id': '3303360b-a642-11ea-aa71-f48e3877e5fc'},
    {'x0': Decimal('64.944'), 'x1': Decimal('96.624'), 'top': Decimal('305.019'), 'bottom': Decimal('315.579'),
     'upright': 1, 'text': '有限售', 'id': '3303360c-a642-11ea-8111-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('235.232'), 'top': Decimal('304.779'), 'bottom': Decimal('315.339'),
     'upright': 1, 'text': '其中：控股股东、实际控制', 'id': '33035d14-a642-11ea-bd8a-f48e3877e5fc'},
    {'x0': Decimal('248.570'), 'x1': Decimal('296.365'), 'top': Decimal('305.690'), 'bottom': Decimal('316.250'),
     'upright': 1, 'text': '26,118,750', 'id': '33035d15-a642-11ea-b993-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('305.690'), 'bottom': Decimal('316.250'),
     'upright': 1, 'text': '51.36%', 'id': '33035d16-a642-11ea-bef1-f48e3877e5fc'},
    {'x0': Decimal('385.990'), 'x1': Decimal('415.305'), 'top': Decimal('305.690'), 'bottom': Decimal('316.250'),
     'upright': 1, 'text': '50,250', 'id': '33035d17-a642-11ea-95ae-f48e3877e5fc'},
    {'x0': Decimal('430.390'), 'x1': Decimal('478.185'), 'top': Decimal('305.690'), 'bottom': Decimal('316.250'),
     'upright': 1, 'text': '26,169,000', 'id': '33035d18-a642-11ea-8c79-f48e3877e5fc'},
    {'x0': Decimal('502.540'), 'x1': Decimal('534.051'), 'top': Decimal('305.690'), 'bottom': Decimal('316.250'),
     'upright': 1, 'text': '51.46%', 'id': '33035d19-a642-11ea-a39a-f48e3877e5fc'},
    {'x0': Decimal('64.944'), 'x1': Decimal('96.624'), 'top': Decimal('320.619'), 'bottom': Decimal('331.179'),
     'upright': 1, 'text': '条件股', 'id': '33035d1a-a642-11ea-a0e1-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('121.220'), 'top': Decimal('320.379'), 'bottom': Decimal('330.939'),
     'upright': 1, 'text': '人', 'id': '33035d1b-a642-11ea-a9cc-f48e3877e5fc'},
    {'x0': Decimal('75.504'), 'x1': Decimal('86.064'), 'top': Decimal('336.219'), 'bottom': Decimal('346.779'),
     'upright': 1, 'text': '份', 'id': '33038426-a642-11ea-9f95-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('194.792'), 'top': Decimal('336.459'), 'bottom': Decimal('347.019'),
     'upright': 1, 'text': '董事、监事、高管', 'id': '33038427-a642-11ea-ade1-f48e3877e5fc'},
    {'x0': Decimal('253.850'), 'x1': Decimal('296.365'), 'top': Decimal('337.370'), 'bottom': Decimal('347.930'),
     'upright': 1, 'text': '4,518,000', 'id': '33038428-a642-11ea-84da-f48e3877e5fc'},
    {'x0': Decimal('322.270'), 'x1': Decimal('353.781'), 'top': Decimal('337.370'), 'bottom': Decimal('347.930'),
     'upright': 1, 'text': '60.25%', 'id': '33038429-a642-11ea-82f4-f48e3877e5fc'},
    {'x0': Decimal('409.990'), 'x1': Decimal('415.344'), 'top': Decimal('337.370'), 'bottom': Decimal('347.930'),
     'upright': 1, 'text': '0', 'id': '3303842a-a642-11ea-b55d-f48e3877e5fc'},
    {'x0': Decimal('435.670'), 'x1': Decimal('478.185'), 'top': Decimal('337.370'), 'bottom': Decimal('347.930'),
     'upright': 1, 'text': '4,518,000', 'id': '3303842b-a642-11ea-a73d-f48e3877e5fc'},
    {'x0': Decimal('507.820'), 'x1': Decimal('534.062'), 'top': Decimal('337.370'), 'bottom': Decimal('347.930'),
     'upright': 1, 'text': '8.88%', 'id': '3303ab36-a642-11ea-b08f-f48e3877e5fc'},
    {'x0': Decimal('110.660'), 'x1': Decimal('152.784'), 'top': Decimal('352.659'), 'bottom': Decimal('363.219'),
     'upright': 1, 'text': '核心员工', 'id': '3303ab37-a642-11ea-bcac-f48e3877e5fc'},
    {'x0': Decimal('291.050'), 'x1': Decimal('296.404'), 'top': Decimal('353.570'), 'bottom': Decimal('364.130'),
     'upright': 1, 'text': '0', 'id': '3303ab38-a642-11ea-9390-f48e3877e5fc'},
    {'x0': Decimal('340.870'), 'x1': Decimal('353.820'), 'top': Decimal('353.570'), 'bottom': Decimal('364.130'),
     'upright': 1, 'text': '0%', 'id': '3303ab39-a642-11ea-b0d9-f48e3877e5fc'},
    {'x0': Decimal('409.990'), 'x1': Decimal('415.344'), 'top': Decimal('353.570'), 'bottom': Decimal('364.130'),
     'upright': 1, 'text': '0', 'id': '3303d248-a642-11ea-864a-f48e3877e5fc'},
    {'x0': Decimal('472.900'), 'x1': Decimal('478.254'), 'top': Decimal('353.570'), 'bottom': Decimal('364.130'),
     'upright': 1, 'text': '0', 'id': '3303d249-a642-11ea-b1c1-f48e3877e5fc'},
    {'x0': Decimal('521.140'), 'x1': Decimal('534.090'), 'top': Decimal('353.570'), 'bottom': Decimal('364.130'),
     'upright': 1, 'text': '0%', 'id': '3303d24a-a642-11ea-8944-f48e3877e5fc'},
    {'x0': Decimal('132.500'), 'x1': Decimal('164.180'), 'top': Decimal('368.739'), 'bottom': Decimal('379.299'),
     'upright': 1, 'text': '总股本', 'id': '3303d24b-a642-11ea-acd8-f48e3877e5fc'},
    {'x0': Decimal('248.570'), 'x1': Decimal('296.365'), 'top': Decimal('369.650'), 'bottom': Decimal('380.210'),
     'upright': 1, 'text': '50,850,000', 'id': '3303d24c-a642-11ea-924d-f48e3877e5fc'},
    {'x0': Decimal('328.750'), 'x1': Decimal('331.981'), 'top': Decimal('369.650'), 'bottom': Decimal('380.210'),
     'upright': 1, 'text': '-', 'id': '3303d24d-a642-11ea-a7d7-f48e3877e5fc'},
    {'x0': Decimal('409.990'), 'x1': Decimal('415.344'), 'top': Decimal('369.650'), 'bottom': Decimal('380.210'),
     'upright': 1, 'text': '0', 'id': '3303d24e-a642-11ea-8baf-f48e3877e5fc'},
    {'x0': Decimal('430.390'), 'x1': Decimal('478.185'), 'top': Decimal('369.650'), 'bottom': Decimal('380.210'),
     'upright': 1, 'text': '50,850,000', 'id': '3303f958-a642-11ea-bcc3-f48e3877e5fc'},
    {'x0': Decimal('509.860'), 'x1': Decimal('513.091'), 'top': Decimal('369.650'), 'bottom': Decimal('380.210'),
     'upright': 1, 'text': '-', 'id': '3303f959-a642-11ea-936b-f48e3877e5fc'},
    {'x0': Decimal('111.500'), 'x1': Decimal('185.420'), 'top': Decimal('384.819'), 'bottom': Decimal('395.379'),
     'upright': 1, 'text': '普通股股东人数', 'id': '3303f95a-a642-11ea-8599-f48e3877e5fc'},
    {'x0': Decimal('523.300'), 'x1': Decimal('534.054'), 'top': Decimal('385.730'), 'bottom': Decimal('396.290'),
     'upright': 1, 'text': '76', 'id': '3303f95b-a642-11ea-9f84-f48e3877e5fc'}
]

#
# @归纳行
# top值相等或相差小于15的就当做同一行
# {'x0': Decimal('289.250'), 'x1': Decimal('310.370'), 'top': Decimal('176.469'), 'bottom': Decimal('187.029'), 'upright': 1, 'text': '期初'}

def takeSecond(item):
    return item['x0']

table = []
json_key = {}
for index, row in enumerate(table_list):
    n = index + 1
    if not json_key.__contains__(row['id']):
        table_row = [row]
        json_key[row['id']] = True
    else:
        continue
    while n < len(table_list):
        next_row = table_list[n]
        if abs(row['top'] - next_row['top']) < 15:
            if not json_key.__contains__(next_row['id']):
                table_row.append(next_row)
                json_key[next_row['id']] = True
        n += 1
    table_row.sort(key=takeSecond)
    table.append(table_row)

print(table)


class ProcessTableRow:

    def __init__(self):
        pass

    def merge_row(self):
        pass



























