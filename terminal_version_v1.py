from search import search
import time
import os
import random 
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import subprocess

path=".\\temp"
window_name = 'image'

key_word = input("Please enter a key word: ")
search.search(key_word, limit=3,  output_dir="temp", verbose=False)

print("Please wait...")
time.sleep(1)
files=os.listdir(path)
while len(files) == 0:
    time.sleep(1)
    files=os.listdir(path)


print("Started")
files=os.listdir(path)
d=random.choice(files)

key = input("Enter a request: next(n), remove(r), save(s) quit(q):\n")
while True:
    if key == "n":
        pass
    elif key == "q":
        break

    
    key = input("Enter a request: next(n), remove(r), save(s) quit(q):\n")


