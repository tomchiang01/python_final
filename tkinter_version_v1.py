
import time
import os, stat
import sys
import random 

import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from search import search
import shutil

# Init
path=os.path.abspath(".\\temp")

filename = ""
S
key_word = ""

root = Tk()
root.geometry("300x400")

save_path = os.path.abspath('saved_images')
if not os.path.exists(save_path):
    os.makedirs(save_path)


# Function for buttons
def next():
    global path, filename
    files=os.listdir(path)
    filename=random.choice(files)
    image1 = Image.open(path+"\\"+filename)
    image1 = image1.resize((300,300))
    test = ImageTk.PhotoImage(image1)

    Image1 = tkinter.Label(image=test)
    Image1.image = test
    # Position image
    Image1.place(x=0, y=100)

def save():
    image_save = Image.open(path+"\\"+filename) 
    
    # save a image using extension

    image_save = image_save.save(save_path+"\\"+filename)
    
def remove():
    os.chmod(path+"\\"+filename, stat.S_IWRITE)
    os.remove(path+"\\"+filename)
    next()
    
def quit():
    global S
    try:
        S.kill()
    except:
        pass
    root.destroy()

def f_search():
    global entry
    if entry.get() != '':
        temp = entry.get()
    print(temp)
    # Start searching
    global S, key_word, path
    if temp != key_word:
        if os.path.exists(path):
            shutil.rmtree(path)
        key_word = temp
    
    print(key_word)
    try:
        S.kill()
    except:
        pass
    S = search.Search(key_word, limit=100,  output_dir="temp", verbose=False)
    print("Please wait...")
    time.sleep(1)
    files=os.listdir(path)
    while len(files) == 0:
        time.sleep(1)
        files=os.listdir(path)

    print("Started")
    # Initial images
    files=os.listdir(path)
    filename=random.choice(files)
    image1 = Image.open(path+"\\"+filename)
    image1 = image1.resize((300,300))
    test = ImageTk.PhotoImage(image1)
    Image1 = tkinter.Label(image=test)
    Image1.image = test
    Image1.place(x=0, y=100)


# Build buttons
entry = Entry(root)
entry.place(x=50, y=10)
B_search = Button(root, text ="search", command = f_search)
B_search.place(x=220, y=10)
B_next = Button(root, text ="next", command = next)
B_next.place(x=50, y=60)
B_quit = Button(root, text ="save", command = save)
B_quit.place(x=100, y=60)
B_quit = Button(root, text ="remove", command = remove)
B_quit.place(x=150, y=60)
B_quit = Button(root, text ="quit", command = quit)
B_quit.place(x=220, y=60)
    

if __name__ == '__main__':
    root.mainloop()
    try:
        S.kill()
    except:
        pass