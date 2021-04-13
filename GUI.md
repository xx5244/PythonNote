# GUI
---

+ ## 定義
  **圖形使用者介面:採用圖形的方式讓使用者直接用圖形來操控程式運行**

+ ## 工具
  **TKinter:此為python內建的GUI製作工具，裡面有各種圖形控制元件可供使用**

+ ## 範例
    ```python
        # GUI範例
        # 座標左上為(0,0)

        import tkinter as tk

        # 建立視窗
        win = tk.Tk()

        # 視窗標題
        win.title('視窗標題')

        # 視窗大小
        width = 800
        height = 600
        win.geometry(f'{width}x{height}')

        # 關閉讓使用者手動改變視窗大小的功能
        win.resizable(width=0, height=0)

        # 背景顏色
        win.config(bg='#000000')

        # 建立Label
        # lbpath = tk.Label(text='影片路徑', bg='#000000', fg='#FFFFFF', font='微軟正黑體 18')
        # lbpath.grid(row=80, column=60)

        # 建立Button
        btn = tk.Button(text='button')
        btn.pack()

        # 常駐視窗
        win.mainloop()
    ```