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
# 参照ボタンを押したときの動作，選択したファイルの絶対パスを取得，ファイルはCSVに指定
def ClickRefButton():
    fTyp = [("CSVファイル","*.csv")]# 入力ファイルの拡張子を指定，今回はCSV
    iDir = os.path.abspath(os.path.dirname(__file__))# このコードがあるファイルの絶対パスを取得
    filepath = filedialog.askopenfilenames(filetypes = fTyp, initialdir = iDir)# ファイルダイアログを表示し，複数ファイルを選択
    # # ファイルリストを作成，参照できるようにグローバル変数にする
    global file_list
    file_list = list(filepath)
    

# Figureボタンを押したときの動作
def ClickedFigureButton ():
    # 読み込んだファイルリストのパスをGenerateFigures()に渡していく
    for path in file_list:
        GenerateFigures(path)
    
    # 計測が終わったら終了メッセージを表示
    messagebox.showinfo("status", "グラフの生成が終わりました．")


# 粘着力の計算とグラフの生成，保存
def GenerateFigures(_path):
    # ファイルパスからファイルの名前を取得
    csv_file_name, ext = os.path.splitext(os.path.basename(_path))
    # 引数ファイルパスを開く
    csv_input = pd.read_csv(filepath_or_buffer = _path,
                        encoding = "utf_8", sep=",", engine="python",
                        header = None)

    # グラフ画像を保存するディレクトリの作成（参照ファイルと同一階層内に作る）
    figure_dir_path = os.path.dirname(_path) + "/" + csv_file_name + "_figures"
    os.mkdir(figure_dir_path)

    #オフセット行を格納
    offset = []
    offset = csv_input.iloc[1,:]

    #lenで行数を取得
    for i in range(len(csv_input)):
    #10行まででテスト
    # for i in range(10):
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


# Peakボタンを押したときの動作
def ClickedPeakButton ():
    # 計算したピーク値とそのフレーム番号を入れるリスト
    peak_list = []
    # 読み込んだファイルリストのパスをPeakAdhesiveForce()に渡していく
    for path in file_list:
        # 要素を追加
        peak_list.append( PeakAdhesiveForce (path) )

    # 計測が終わったら終了メッセージを表示
    messagebox.showinfo("status", "ピーク値の計算が終わりました．{}".format(peak_list))


# 粘着力のピーク値を計算する
def PeakAdhesiveForce(_path):
    # 参照ファイル（file1）を開く
    csv_input = pd.read_csv(filepath_or_buffer=  _path,
                        encoding = "utf_8", sep=",", engine="python",
                        header = None)
    
    # 両端を省略したオフセット行を格納
    offset = []
    offset = csv_input.iloc[1,1:16]

    # global peak_force # peak_forceがglobal変数であることを指示
    peak_force = 0 # peak_forceの宣言
    peak_flame = 0 # peak_flameの宣言

    #lenで行数を取得
    for i in range(len(csv_input)):
    #100行まででテスト
    # for i in range(100):
        # 両端を省略した差分を計算
        adhesive_force_list = offset - csv_input.iloc[i,1:16]
        # 最大値の表示
        # print(max(adhesive_force_list))
        temp_peak_force =max(adhesive_force_list)
        # 最大値の更新
        if temp_peak_force > peak_force:
            peak_force = temp_peak_force
            peak_flame = i

    # ピーク値とフレーム番号を返す
    return (peak_force, peak_flame)

# Resetボタンを押したときの挙動
def ClickedResetButton():
    file_list = 0
    print(file_list)
    messagebox.showinfo("reset","ファイルパスをリセットしました")


# GUIrootの作成
root = tk.Tk()
root.title('CalcAdhesiveForce')
root.resizable(False, False)#リサイズの無効化

# Frame1の作成
frame1 = ttk.Frame(root, padding = 10)
frame1.grid()

# 参照ボタンの作成
ref_button = ttk.Button(root, text = u'参照', command = ClickRefButton )
ref_button.grid(row = 0, column = 3)

# ラベルの作成
# 「ファイル」ラベルの作成
s = StringVar()
s.set('ファイル>>')
label1 = ttk.Label(frame1, textvariable=s)
label1.grid(row=0, column=0)

# 参照ファイルパス表示ラベルの作成
file_list = StringVar()
file_list_entry = ttk.Entry(frame1, textvariable=file_list, width=50)
file_list_entry.grid(row=0, column=2)

# Frame2の作成
frame2 = ttk.Frame(root, padding=(0,5))
frame2.grid(row=1)

# Figureボタンの作成
figure_button = ttk.Button(frame2, text='Generate Figures', command = ClickedFigureButton )
figure_button.pack(side=LEFT)

# Peak Valueボタンの作成
peak_button = ttk.Button(frame2, text='Calc Peak Value', command=ClickedPeakButton)
peak_button.pack(side=LEFT)

# Cancelボタンの作成
cancel_button = ttk.Button(frame2, text='Cancel', command=quit)
cancel_button.pack(side=LEFT)

# Resetボタンの作成
reset_button = ttk.Button(frame2, text='Reset', command=ClickedResetButton)
reset_button.pack(side=LEFT)

root.mainloop()