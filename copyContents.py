# Print all files in cwd starting with a letter character
# Copies printed files to the clipboard with new lines included
import os
from tkinter import filedialog
from tkinter import *
import pyperclip

target = filedialog.askdirectory()

file_list = set()
for f in os.listdir(target):
    if f[0].isalpha():
        file_list.add(f)

file_list.discard("copyContents.py")
copy = ""
for file in file_list:
    copy = copy + file + "\n"
    print(file)
pyperclip.copy(copy)