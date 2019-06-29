# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:36:39 2019

@author: TKameoka

参考：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869

"""

import csv

csv_file = open("./20190626194837.csv", encoding = "utf_8", newline="")

#リスト形式

f = csv.reader(csv_file, delimiter = ",", doublequote = True, lineterminator = "\r\n", quotechar = '"', skipinitialspace = True)
"""
delimiter:区切り文字
doublequote:
"""

header = next(f)
print(header)
for row in f:    
    print(row)