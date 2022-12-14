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
        
        self.l_img_refresh_time = tk.Label(self.master, text = "圖片刷新時間: ")
        self.l_img_refresh_time.place(x = 10, y = 40)
        self.e_img_refresh_time_text = tk.StringVar()
        self.e_img_refresh_time = tk.Entry(self.master, width = 15, textvariable=self.e_img_refresh_time_text)
        self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time))
        if self.widget.img_refresh_time <= 0:
            self.widget.img_refresh_time = 0
            self.e_img_refresh_time_text.set("0")
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
        
        self.l_temp_refresh_time = tk.Label(self.master, text = "圖庫更新時間: ")
        self.l_temp_refresh_time.place(x = 10, y = 100)
        self.e_temp_refresh_time_text = tk.StringVar()
        self.e_temp_refresh_time = tk.Entry(self.master,width = 15,textvariable=self.e_temp_refresh_time_text)
        self.e_temp_refresh_time_text.set(str(self.widget.picdict_refresh_time))
        self.e_temp_refresh_time.place(x = 100, y = 100)
        self.l_temp_refresh_time2 = tk.Label(self.master, text = "分鐘")
        self.l_temp_refresh_time2.place(x = 210, y = 100)
        
        self.l_userDir = tk.Label(self.master, text = "自訂存放位置: ")
        self.l_userDir.place(x = 10, y = 130)
        self.b_set_userDir = tk.Button(self.master, text ="瀏覽", command = self.findUserDir)
        self.b_set_userDir.place(x = 250, y = 130)
        self.e_userDir_text = tk.StringVar()
        self.e_userDir_text.set(str(self.widget.user_save_dir))
        self.e_userDir = tk.Entry(self.master, textvariable=self.e_userDir_text)
        self.e_userDir.place(x = 100, y = 130)

        #self.b_set_temp_size = tk.Button(self.master, text ="確定", command = self.set_temp_size)
        #self.b_set_temp_size.place(x = 250, y = 68)
        
        self.b_set_all = tk.Button(self.master, text ="OK", command = self.set_all)
        self.b_set_all.place(x = 200, y = 250)
        
        self.b_cancel = tk.Button(self.master, text ="cancel", command = self.master.destroy)
        self.b_cancel.place(x = 235, y = 250)
        
    def set_all(self):
        self.set_time()
        self.set_temp_size()
        self.set_Dir()
        self.set_picdict_refresh_time()
        
        
    def set_time(self):
        try:
            self.widget.img_refresh_time = float((self.e_img_refresh_time_text.get().split()[0]))
            self.e_img_refresh_time_text.set(str(self.widget.img_refresh_time))
            if self.widget.img_refresh_time <= 0:
                self.widget.img_refresh_time = 0
                self.e_img_refresh_time_text.set("0")
        
            if self.widget.img_refresh_time != 0:
                try:
                    self.widget.alarm.cancel()
                except:
                    pass
                self.widget.alarm = threading.Timer(self.widget.img_refresh_time * 60, self.widget.next)
                self.widget.alarm.start()
        except:
            self.e_img_refresh_time_text.set('輪入格式錯誤')

            
        
    def set_temp_size(self):
        try:
            self.widget.temp_size = int((self.e_temp_size.get().split())[0])
            self.e_temp_size_text.set(str(self.widget.temp_size))
            if self.widget.temp_size <= 0:
                self.widget.temp_size = 0
                self.e_temp_size_text.set('0')
        except:
            self.e_temp_size_text.set('輪入格式錯誤')
            
    def findUserDir(self):
        
        dirName = tkinter.filedialog.askdirectory(
                                          title = "Select a Folder",
                                          )
        self.master.lift()
        self.e_userDir_text.set(dirName)
        
        
        
    def set_Dir(self):
        try:
            self.widget.user_save_dir = self.e_userDir_text.get()
        except:
            self.e_userDir_text.set('輪入格式錯誤')
            
    def set_picdict_refresh_time(self):
        try:
            self.widget.picdict_refresh_time = float((self.e_temp_refresh_time_text.get().split())[0])
            self.e_temp_refresh_time_text.set(str(self.widget.picdict_refresh_time))
            if self.widget.picdict_refresh_time <= 0:
                self.widget.picdict_refresh_time = 0
                self.e_temp_refresh_time_text.set("永不")

            
            if self.widget.picdict_refresh_time != 0:
                try:
                    self.widget.alarm1.cancel()
                except:
                    pass
                self.widget.alarm1 = threading.Timer(self.widget.picdict_refresh_time * 60, self.widget.refresh_picdict)
                self.widget.alarm1.start()
        except:
            self.e_temp_refresh_time_text.set('輪入格式錯誤')
        