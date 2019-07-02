# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:02:43 2019

@author: Takayuki
"""

# Tkinterのライブラリを取り込む --- (*1)
import tkinter as tk
from tkinter import messagebox as mbox

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("Hello, World!") # タイトル
win.geometry("400x300") # サイズ

#
# ラベル作成
label = tk.Label(win, text="名前は？")
label.pack()

#テキストボックスを作成
text = tk.Entry(win)
text.pack()
text.insert(tk.END, 'クジラ') #初期値を設定

#OKボタンを押したときの処理
def OkClick():
    #テキストボックスの中身を見る
    s = text.get()
    #ダイアログを表示
    mbox.showinfo('挨拶', s + 'さん，こんにちは！')

#ボタンを作成
ok_button = tk.Button(win, text = "OK!",  command = OkClick)
ok_button.pack()

# ウィンドウを動かす --- (*3)
win.mainloop()