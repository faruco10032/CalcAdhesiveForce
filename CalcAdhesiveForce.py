# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:02:02 2019

@author: TKameoka

"""

import os # make directry
import matplotlib # make figures
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd # read CSV
import tkinter as tk # GUI liblary
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# GUIの作成
# 参照ボタンを押したときの動作，選択したファイルの拡張子と絶対パスを取得
def ClickRefButton():
    fTyp = [("CSVファイル","*.csv")]# 入力ファイルの拡張子を指定，今回はCSV
    iDir = os.path.abspath(os.path.dirname(__file__))# このコードがあるファイルの絶対パスを取得
    filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)# ファイルダイアログを表示
    file1.set(filepath)# file1に絶対パスをセット


# 粘着力の計算とグラフの生成，保存
# 後で別関数に分けたほうがいいかも
# CSVファイルパスを引数にしたほうがいい？（.set()，.get()を理解しきれていない）
def GenerateFigures():

    # csv_file_name = "20190626194837"
    # ファイル名と拡張子を取得する
    csv_file_name, ext = os.path.splitext(os.path.basename(file1.get()))

    # filepath_name = "./" + csv_file_name + ".csv"
    # csv_input = pd.read_csv(filepath_or_buffer= filepath_name ,
    #                     encoding = "utf_8", sep=",", engine="python",
    #                     header = None)
    # 参照ファイル（file1）を開く
    csv_input = pd.read_csv(filepath_or_buffer=  file1.get(),
                        encoding = "utf_8", sep=",", engine="python",
                        header = None)

    # グラフ画像を保存するディレクトリの作成（参照ファイルと同一階層内に作る）
    # figure_dir_path = "./" + csv_file_name + "_figures"
    figure_dir_path = os.path.dirname(file1.get()) + "/" + csv_file_name + "_figures"
    os.mkdir(figure_dir_path)

    #オフセット行を格納
    offset = []
    offset = csv_input.iloc[1,:]

    #lenで行数を取得
    # for i in range(len(csv_input)):
    #10行まででテスト
    for i in range(10):
    #    print(csv_input.iloc[i,:]-offset)
        #オフセット値から各計測地を減算して表示
        plt.plot(offset - csv_input.iloc[i,:], marker = "o")
        plt.ylim([-5,40])#Y軸の幅を指定
        plt.title(i)#タイトルをフレーム数にする
        plt.xlabel("X-axis")#x軸の名前．
        plt.ylabel("Y-axis")#y軸の名前．あとで力（mN）にする
        file_name ="{0:03d}".format(i) + '.png' #3桁の連版の名前をつける
        plt.savefig(figure_dir_path + "/" + file_name)
        plt.figure()

    # 計測が終わったら終了メッセージを表示
    messagebox.showinfo("status", "解析が終わりました．")

# GUIrootの作成
root = tk.Tk()
root.title('CalcAdhesiveForce')
root.resizable(False, False)#リサイズの無効化

# Frame1の作成
frame1 = ttk.Frame(root, padding = 10)
frame1.grid()

# 参照ボタンの作成
ref_button = ttk.Button(root, text = u'参照', command = ClickRefButton)
ref_button.grid(row = 0, column = 3)

# ラベルの作成
# 「ファイル」ラベルの作成
s = StringVar()
s.set('ファイル>>')
label1 = ttk.Label(frame1, textvariable=s)
label1.grid(row=0, column=0)

# 参照ファイルパス表示ラベルの作成
file1 = StringVar()
file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
file1_entry.grid(row=0, column=2)

# Frame2の作成
frame2 = ttk.Frame(root, padding=(0,5))
frame2.grid(row=1)

# Startボタンの作成
start_button = ttk.Button(frame2, text='Start', command=GenerateFigures)
start_button.pack(side=LEFT)

# Cancelボタンの作成
cancel_button = ttk.Button(frame2, text='Cancel', command=quit)
cancel_button.pack(side=LEFT)

root.mainloop()