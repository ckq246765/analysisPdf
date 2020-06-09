#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import tabula

# Read pdf into list of DataFrame
df = tabula.read_pdf("test.pdf", pages='all')
print(df)

# Read remote pdf into list of DataFrame
df2 = tabula.read_pdf("test.pdf")
print(df2)

# convert PDF into CSV file
tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch("./", output_format='csv', pages='all')
print('--------------------end---------------------')