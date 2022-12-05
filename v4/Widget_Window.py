import tkinter as tk
import threading
import os
import random
from PIL import Image, ImageTk
from Setting_Window import Setting_Window
import search
import shutil
import stat

class Widget_Window:
    def __init__(self, master):
        self.key_word = ''
        self.img_refresh_time = 0
        self.downloader = None
        self.filename = ''
        self.picdict = []
        self.picid = 0
        self.ready = False
        self.user_save_dir = os.path.abspath('saved_images')

        path = os.path.abspath(".\\temp")
        if os.path.exists(path):
            shutil.rmtree(path)
            

        self.master = master
        self.master.title("Widget")
        self.master.geometry("300x350")
        self.temp_size = 20
        self.b_setting = tk.Button(self.master, text = '設定', command = self.open_setting)
        self.b_setting.place(x = 240, y = 8)

        
        self.b_next = tk.Button(self.master, text ="→", command = self.next)
        self.b_next.place(x=50, y=10)
        self.b_last = tk.Button(self.master, text ="←", command = self.last)
        self.b_last.place(x=10, y=10)
        self.b_shuffle = tk.Button(self.master, text ="🔀", command = self.shuffle)
        self.b_shuffle.place(x=90, y=10)
        self.b_save = tk.Button(self.master, text ="儲存", command = self.save)
        self.b_save.place(x=140, y=10)
        self.b_remove = tk.Button(self.master, text ="移除", command = self.remove)
        self.b_remove.place(x=190, y=10)
        
        self.l_key_word = tk.Label(self.master, text = "主題: ")
        self.l_key_word.place(x = 10, y = 50)
        self.e_key_word_text = tk.StringVar()
        self.e_key_word = tk.Entry(self.master, textvariable=self.e_key_word_text)
        if self.key_word == "":
            self.e_key_word_text.set("請輸入")
        else:
            self.e_key_word_text.set(self.key_word)
        self.e_key_word.place(x = 50, y = 50)
        self.b_set_temp_size = tk.Button(self.master, text ="確定", command = self.set_key_word)
        self.b_set_temp_size.place(x = 200, y = 50)


    def open_setting(self):
        self.newWindow = tk.Toplevel(self.master)
        self.setting_window = Setting_Window(self.newWindow, self)

    def next(self):
        if self.ready:
            self.refresh_img(next=1)
            
    def last(self):
        if self.ready:
            self.refresh_img(next=0)
            
    def shuffle(self):
        if self.ready:
            self.refresh_img(next=2)
    
    def save(self):
        if self.ready:
            path = os.path.abspath(".\\temp")
            image_save = Image.open(path+"\\"+self.filename) 
            
            # save a image using extension
            # save_path = os.path.abspath('saved_images')
            save_path = self.user_save_dir
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            image_save = image_save.save(save_path+"\\"+self.filename)
        
    def remove(self):
        if self.ready:
            path = os.path.abspath(".\\temp")
            os.chmod(path+"\\"+self.filename, stat.S_IWRITE)
            os.remove(path+"\\"+self.filename)
            del self.picdict[self.id]
            self.next()
        
    def refresh_img(self, next=-1):
        path = os.path.abspath(".\\temp")
        if not os.path.exists(path):
            os.makedirs(path)

        # files = os.listdir(path)
        self.picdict = os.listdir(path)
        if len(self.picdict) != 0:
            try:
                self.Image1.config(image='')
            except:
                pass
            temp = self.choose_picture(next=next)
            self.filename = temp
            image1 = Image.open(path+"\\"+self.filename)
            w,h = image1.size
            if(w>h):
                t = 300/w
            else:
                t = 300/h
            w, h = int(w*t), int(h*t)
            image1 = image1.resize((w,h))
            test = ImageTk.PhotoImage(image1)
            self.Image1 = tk.Label(image=test)
            self.Image1.image = test
            self.Image1.place(x=int((300-w-5)/2), y=75+int((300-h)/2))

            self.ready = True

            if self.img_refresh_time != 0:
                try:
                    self.alarm.cancel()
                except:
                    pass
                self.alarm = threading.Timer(self.img_refresh_time * 60, self.refresh_img)
                self.alarm.start()
        else:
            self.alarm = threading.Timer(1, self.refresh_img)
            self.alarm.start()


    def kill(self):
        try:
            self.alarm.cancel()
        except:
            pass
        try:
            self.downloader.kill()
        except:
            pass
        
    def set_key_word(self):
        path=os.path.abspath(".\\temp")
        temp = self.e_key_word.get()
        if temp != self.key_word:
            if os.path.exists(path):
                shutil.rmtree(path)
            self.key_word = temp
        self.picid = 0
        try:
            self.downloader.kill()
        except:
            pass
        self.downloader = search.Search(self.key_word, limit=self.temp_size,  output_dir="temp", verbose=False)
        
        self.e_key_word_text.set(self.key_word)
        self.refresh_img()
        
    def choose_picture(self, next:bool):
        # temp = random.choice(files)
        # while(len(files) > 1 and temp == self.filename):
        #     temp = random.choice(files)
        if next==1:
            self.picid = (self.picid + 1) % len(self.picdict)
        elif next==0:
            self.picid = (self.picid + len(self.picdict) - 1) % len(self.picdict)
        elif next== -1:
            pass
        else:
            temp_id = self.picid
            while temp_id == self.picid:
                temp_id = random.randint(0,len(self.picdict)-1)
            self.picid = temp_id
        return self.picdict[self.picid]
