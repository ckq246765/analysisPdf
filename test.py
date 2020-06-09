#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json

_str = '.x2{left:61.560000px;}'
res = re.findall('(?<=:).*(?=p)', _str)
print(res)

obj = {'a': 1, 'b': 2}

a,b = obj
print(a, b)