import tkinter as tk
import os
import shutil
import search
import threading

class Setting_Window:
    def __init__(self, master, widget):
        self.master = master
        self.widget = widget
        self.master.title("設定")
        self.master.geometry("300x300")
        self.l_key_word = tk.Label(self.master, text = "關鍵字: ")
        self.l_key_word.place(x = 10, y = 10)
        self.e_key_word_text = tk.StringVar()
        self.e_key_word = tk.Entry(self.master, textvariable=self.e_key_word_text)
        if self.widget.key_word == "":
            self.e_key_word_text.set("未設定")
        else:
            self.e_key_word_text.set(self.widget.key_word)
        self.e_key_word.place(x = 100, y = 10)
        
        self.b_set_key = tk.Button(self.master, text ="確定", command = self.set_key_word)
        self.b_set_key.place(x = 250, y = 8)
        
        self.l_img_refresh_time = tk.Label(self.master, text = "圖片刷新時間: ")
        self.l_img_refresh_time.place(x = 10, y = 40)
        self.e_img_refresh_time_text = tk.StringVar()
        self.e_img_refresh_time = tk.Entry(self.master, textvariable=self.e_img_refresh_time_text)
        self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time) + " 分鐘")
        if self.widget.img_refresh_time <= 0:
            self.widget.img_refresh_time = 0
            self.e_img_refresh_time_text.set("永不")
        self.e_img_refresh_time.place(x = 100, y = 40)
        
        self.b_set_time = tk.Button(self.master, text ="確定", command = self.set_time)
        self.b_set_time.place(x = 250, y = 38)


        self.l_temp_size = tk.Label(self.master, text = "圖庫大小: ")
        self.l_temp_size.place(x = 10, y = 70)
        self.e_temp_size_text = tk.StringVar()
        self.e_temp_size = tk.Entry(self.master, textvariable=self.e_temp_size_text)
        self.e_temp_size_text.set(str(self.widget.temp_size))
        self.e_temp_size.place(x = 100, y = 70)

        self.b_set_temp_size = tk.Button(self.master, text ="確定", command = self.set_temp_size)
        self.b_set_temp_size.place(x = 250, y = 68)

    def set_key_word(self):
        path=os.path.abspath(".\\temp")
        temp = self.e_key_word.get()
        if temp != self.widget.key_word:
            if os.path.exists(path):
                shutil.rmtree(path)
            self.widget.key_word = temp
            
        try:
            self.widget.downloader.kill()
        except:
            pass
        self.widget.downloader = search.Search(self.widget.key_word, limit=self.widget.temp_size,  output_dir="temp", verbose=False)
        
        self.e_key_word_text.set(self.widget.key_word)
        self.widget.refresh_img()
        
        
    def set_time(self):
        try:
            self.widget.img_refresh_time = float((self.e_img_refresh_time.get().split())[0])
            self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time) + " 分鐘")
            if self.widget.img_refresh_time <= 0:
                self.widget.img_refresh_time = 0
                self.e_img_refresh_time_text.set("永不")

            
            if self.widget.img_refresh_time != 0:
                try:
                    self.widget.alarm.cancel()
                except:
                    pass
                self.widget.alarm = threading.Timer(self.widget.img_refresh_time * 60, self.widget.refresh_img)
                self.widget.alarm.start()
        except:
            self.e_img_refresh_time_text.set('輪入格式錯誤')

            
        
    def set_temp_size(self):
        try:
            self.widget.temp_size = int((self.e_temp_size.get().split())[0])
            self.e_temp_size_text.set(str(self.widget.temp_size))
            if self.widget.temp_size <= 0:
                self.widget.temp_size = 1
                self.e_temp_size_text.set('輪入格式錯誤')

            
        except:
            self.e_temp_size_text.set('輪入格式錯誤')