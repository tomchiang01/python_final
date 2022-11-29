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
        self.refresh_time = 0
        self.downloader = None
        self.filename = ''
        self.ready = False

        path = os.path.abspath(".\\temp")
        if os.path.exists(path):
            shutil.rmtree(path)

        self.master = master
        self.master.title("Widget")
        self.master.geometry("300x350")
        self.l_key1 = tk.Label(self.master, text = "Key Word: ")
        self.l_key1.place(x = 10, y = 10)
        self.l_key2 = tk.Label(self.master, text = "None")
        self.l_key2.place(x = 75, y = 10)
        self.l_time1 = tk.Label(self.master, text = "Refresh Time: ")
        self.l_time1.place(x = 10, y = 40)
        self.l_time2 = tk.Label(self.master, text = "Never")
        self.l_time2.place(x = 90, y = 40)
        self.b_setting = tk.Button(self.master, text = 'setting', command = self.open_setting)
        self.b_setting.place(x = 240, y = 8)

        
        self.b_next = tk.Button(self.master, text ="next", command = self.next)
        self.b_next.place(x=50, y=70)
        self.b_save = tk.Button(self.master, text ="save", command = self.save)
        self.b_save.place(x=120, y=70)
        self.b_remove = tk.Button(self.master, text ="remove", command = self.remove)
        self.b_remove.place(x=190, y=70)


    def open_setting(self):
        self.newWindow = tk.Toplevel(self.master)
        self.setting_window = Setting_Window(self.newWindow, self)

    def next(self):
        if self.ready:
            self.refresh_img()
    
    def save(self):
        if self.ready:
            path = os.path.abspath(".\\temp")
            image_save = Image.open(path+"\\"+self.filename) 
            
            # save a image using extension

            save_path = os.path.abspath('saved_images')
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            image_save = image_save.save(save_path+"\\"+self.filename)
        
    def remove(self):
        if self.ready:
            path = os.path.abspath(".\\temp")
            os.chmod(path+"\\"+self.filename, stat.S_IWRITE)
            os.remove(path+"\\"+self.filename)
            self.next()
        
    def refresh_img(self):
        path = os.path.abspath(".\\temp")
        if not os.path.exists(path):
            os.makedirs(path)

        files = os.listdir(path)
        if len(files) != 0:
            temp = random.choice(files)
            while(len(files) > 1 and temp == self.filename):
                temp = random.choice(files)
            self.filename = temp
            image1 = Image.open(path+"\\"+self.filename)
            image1 = image1.resize((300,300))
            test = ImageTk.PhotoImage(image1)
            self.Image1 = tk.Label(image=test)
            self.Image1.image = test
            self.Image1.place(x=0, y=100)

            self.ready = True

            if self.refresh_time != 0:
                try:
                    self.alarm.cancel()
                except:
                    pass
                self.alarm = threading.Timer(self.refresh_time * 60, self.refresh_img)
                self.alarm.start()
        else:
            self.alarm = threading.Timer(1, self.refresh_img)
            self.alarm.start()



    def kill(self):
        self.alarm.cancel()
        try:
            self.downloader.kill()
        except:
            pass
