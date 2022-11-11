import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.withdraw() # 隱藏根視窗

messagebox.showinfo('title', 'content') # 顯示訊息對話框
messagebox.showwarning('title', 'content') # 警告訊息對話框
messagebox.showerror('title', 'content') # 錯誤訊息對話框
messagebox.askokcancel('title', 'content') # 確定/取消訊息對話框
messagebox.askquestion('title', 'content') # 是/否訊息對話框

"""
判斷使用者選擇確定/取消/是/否，只要把結果丟進變數裡，判斷變數內容即可
"""