import tkinter as tk
import os
import shutil
import search
import threading

class Setting_Window:
    def __init__(self, master, widget):
        self.master = master
        self.widget = widget
        self.master.title("Setting")
        self.master.geometry("300x300")
        self.l_key_word = tk.Label(self.master, text = "Key Word: ")
        self.l_key_word.place(x = 10, y = 10)
        self.e_key_word = tk.Entry(self.master)
        self.e_key_word.place(x = 100, y = 10)
        self.b_set_key = tk.Button(self.master, text ="set", command = self.set_key_word)
        self.b_set_key.place(x = 250, y = 8)
        
        self.l_refresh_time = tk.Label(self.master, text = "Refresh Time: ")
        self.l_refresh_time.place(x = 10, y = 40)
        self.e_refresh_time_text = tk.StringVar()
        self.e_refresh_time = tk.Entry(self.master, textvariable=self.e_refresh_time_text)
        self.e_refresh_time.place(x = 100, y = 40)
        self.b_set_time = tk.Button(self.master, text ="set", command = self.set_time)
        self.b_set_time.place(x = 250, y = 38)

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
        self.widget.downloader = search.Search(self.widget.key_word, limit=100,  output_dir="temp", verbose=False)
        
        self.widget.l_key2["text"] = self.widget.key_word
        self.widget.refresh_img()
        
        
    def set_time(self):
        try:
            self.widget.refresh_time = int(self.e_refresh_time.get())
            self.widget.l_time2["text"] = str(self.widget.refresh_time) + " min"
            if self.widget.refresh_time <= 0:
                self.widget.refresh_time = 0
                self.widget.l_time2["text"] = "Never"


            
            if self.widget.refresh_time != 0:
                try:
                    self.widget.alarm.cancel()
                except:
                    pass
                self.widget.alarm = threading.Timer(self.widget.refresh_time * 60, self.widget.refresh_img)
                self.widget.alarm.start()
        except:
            self.e_refresh_time_text.set('error input')