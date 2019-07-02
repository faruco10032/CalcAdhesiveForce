# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:02:02 2019

@author: TKameoka

参考：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869
"""

import pandas as pd
csv_input = pd.read_csv(filepath_or_buffer="./20190626194837.csv", encoding = "utf_8", sep=",", engine="python")

#インプットの項目数（行数＊カラム数）を返す
print(csv_input.size)
print(csv_input.values)
print(csv_input.values[1,0])

print(csv_input.head(0))

print(len(csv_input))

print(len(csv_input.columns))

print(csv_input.shape)


# =============================================================================
# データアクセスの方法いろいろ
# loc[rows, columns]
# 全行選択の場合、rowsは「:」を指定
# 
# =============================================================================

print()