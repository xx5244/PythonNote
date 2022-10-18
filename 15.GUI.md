# GUI
---

+ ## 定義
  **圖形使用者介面:採用圖形的方式讓使用者直接用圖形來操控程式運行**

+ ## 工具
  **TKinter:此為python內建的GUI製作工具，裡面有各種圖形控制元件可供使用**

+ ## 佈局
  + ### pack跟grid佈局會衝突
  + ### place佈局與其餘兩個佈局都能相容

+ ## 範例
    ```python
    # GUI範例
    # 座標左上為(0,0)

    import tkinter as tk


    def change_label():
        new_label = en.get()    # 獲取輸入值
        lb.config(text=new_label)  # 修改其參數


    # 建立視窗
    win = tk.Tk()

    # 視窗標題
    win.title('視窗標題')

    # 視窗大小
    width = 800
    height = 600

    # 螢幕的解析度
    screen_width, screen_heigh = win.maxsize()
    center_width = (screen_width - width) // 2
    center_heigh = (screen_heigh - height) // 2

    # 視窗參數值設定
    win.geometry(f'{width}x{height}+{center_width}+{center_heigh}')

    # 關閉讓使用者手動改變視窗大小的功能
    win.resizable(width=False, height=False)

    # icon，一定要式ico檔
    win.iconbitmap(r"C:\Users\xx524\Desktop\IG.ico")

    # 背景顏色
    win.config(bg='#000000')

    # 透明度，1即不透明，0即全透明
    win.attributes('-alpha', 0.7)

    # 置頂
    win.attributes('-topmost', True)

    # 建立Label
    lb = tk.Label(text='影片路徑', bg='#000000', fg='#FFFFFF', font='微軟正黑體 18')
    lb.pack()
    # lbpath.grid(row=80, column=60)

    # 建立entry
    en_text = tk.StringVar()
    en_text.set('請輸入欲修改的label')
    en = tk.Entry(win, textvariable=en_text, font='微軟正黑體 18')
    en.pack()

    # 建立Button
    btn = tk.Button(text='button', command=change_label)
    btn.pack()


    # 常駐視窗
    win.mainloop()
    ```