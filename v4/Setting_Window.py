import tkinter as tk
import tkinter.filedialog
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
        self.l_key_word = tk.Label(self.master, text = "主題: ")
        self.l_key_word.place(x = 10, y = 10)
        self.e_key_word_text = tk.StringVar()
        self.e_key_word = tk.Entry(self.master, textvariable=self.e_key_word_text)
        if self.widget.key_word == "":
            self.e_key_word_text.set("未設定")
        else:
            self.e_key_word_text.set(self.widget.key_word)
        self.e_key_word.place(x = 100, y = 10)
        
        #self.b_set_key = tk.Button(self.master, text ="確定", command = self.set_key_word)
        #self.b_set_key.place(x = 250, y = 8)
        
        self.l_img_refresh_time = tk.Label(self.master, text = "圖片刷新時間: ")
        self.l_img_refresh_time.place(x = 10, y = 40)
        self.e_img_refresh_time_text = tk.StringVar()
        self.e_img_refresh_time = tk.Entry(self.master, width = 15, textvariable=self.e_img_refresh_time_text)
        self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time))
        if self.widget.img_refresh_time <= 0:
            self.widget.img_refresh_time = 0
            self.e_img_refresh_time_text.set("永不")
        self.e_img_refresh_time.place(x = 100, y = 40)
        self.l_img_refresh_time2 = tk.Label(self.master, text = "分鐘")
        self.l_img_refresh_time2.place(x = 210, y = 40)
        
        #self.b_set_time = tk.Button(self.master, text ="確定", command = self.set_time)
        #self.b_set_time.place(x = 250, y = 38)


        self.l_temp_size = tk.Label(self.master, text = "圖庫大小: ")
        self.l_temp_size.place(x = 10, y = 70)
        self.e_temp_size_text = tk.StringVar()
        self.e_temp_size = tk.Entry(self.master, textvariable=self.e_temp_size_text)
        self.e_temp_size_text.set(str(self.widget.temp_size))
        self.e_temp_size.place(x = 100, y = 70)
        
        self.l_userDir = tk.Label(self.master, text = "自訂存放位置: ")
        self.l_userDir.place(x = 10, y = 100)
        self.b_set_userDir = tk.Button(self.master, text ="瀏覽", command = self.findUserDir)
        self.b_set_userDir.place(x = 250, y = 100)
        self.e_userDir_text = tk.StringVar()
        self.e_userDir_text.set(str(self.widget.user_save_dir))
        self.e_userDir = tk.Entry(self.master, textvariable=self.e_userDir_text)
        self.e_userDir.place(x = 100, y = 100)

        #self.b_set_temp_size = tk.Button(self.master, text ="確定", command = self.set_temp_size)
        #self.b_set_temp_size.place(x = 250, y = 68)
        
        self.b_set_all = tk.Button(self.master, text ="OK", command = self.set_all)
        self.b_set_all.place(x = 200, y = 250)
        
        self.b_cancel = tk.Button(self.master, text ="cancel", command = self.master.destroy)
        self.b_cancel.place(x = 235, y = 250)
        
    def set_all(self):
        self.set_key_word()
        self.set_time()
        self.set_temp_size()
        self.set_Dir()
        

    def set_key_word(self):
        path=os.path.abspath(".\\temp")
        temp = self.e_key_word.get()
        if temp != self.widget.key_word:
            if os.path.exists(path):
                shutil.rmtree(path)
            self.widget.key_word = temp
        self.widget.picid = 0
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
            self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time))
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
            
    def findUserDir(self):
        dirName = tkinter.filedialog.askdirectory(
                                          title = "Select a Folder",
                                          )
        self.e_userDir_text.set(dirName)
        
        
    def set_Dir(self):
        try:
            self.widget.user_save_dir = self.e_userDir_text.get()
        except:
            self.e_userDir_text.set('輪入格式錯誤')
        