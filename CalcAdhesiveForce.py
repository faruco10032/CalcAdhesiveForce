# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:02:02 2019

@author: TKameoka

参考：
CSV読み込み：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869
データプロット：http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816

"""

#import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
csv_input = pd.read_csv(filepath_or_buffer="./20190626194837.csv" ,
                        encoding = "utf_8", sep=",", engine="python",
                        header = None)

#インプットの項目数（行数＊カラム数）を返す
#print(csv_input.size)
#print(csv_input.values)
#
#print(len(csv_input))
#
#print(len(csv_input.columns))
#
#print(csv_input.shape)

#print(csv_input.values[0,0])
#print(csv_input.values[0,1])

#print(csv_input.iloc[1,:])
offset = []
offset = csv_input.iloc[1,:]

#print(offset)
#
#print(csv_input[3:4])

#lenで行数を取得
#for i in range(len(csv_input)):
for i in range(10):
#    print(csv_input.iloc[i,:]-offset)
    #オフセット値から各計測地を減算して表示
    plt.plot(offset - csv_input.iloc[i,:], marker = "o")
    plt.ylim([-5,40])
    plt.title(i)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
#    plt.show()
    file_name ="{0:03d}".format(i) + '.png'
    plt.savefig(file_name)
    plt.figure()
   
print(len(csv_input))

#plt.plot(csv_input.iloc[2,:] - offset)
#plt.show()