# User is prompted to specify target directory
# Text files are generated for each subdirectory, containing it's full path and contained files
# Corresponding subdirectory names are printed to console (Redundant if using bat file)

import os
from tkinter import filedialog
from tkinter import *
import shutil

# CONFIG
MAX_OUTPUT_DIR_SIZE = 20000
output_path = os.getcwd() + "/contentsToFile-output"


# Returns size of given directory
def dir_size(path):
    #initialize the size
    total_size = 0
    #use the walk() method to navigate through directory tree
    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:
            #use join to concatenate all the components of path
            f = os.path.join(dirpath, i)
            #use getsize to generate size in bytes and add it to the total size
            total_size += os.path.getsize(f)
    return total_size

    

target = filedialog.askdirectory()
if dir_size(output_path) > MAX_OUTPUT_DIR_SIZE:
    print("ERROR: Output directory contents are too large! Check why...")
    print("Exiting...")
    quit()

# Quit if directory selection dialog is closed without a selection
if len(target) < 1:
    quit()

# Ensure output folder exists
print("About to remove and overwrite the following folder:")
print(output_path)
if input("Continue? (type 'continue' to confirm)\n> ") == "continue":
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)
    os.chdir(output_path)
else:
    print("Quitting script... don't worry! No changes made.")
    quit()

# Collect required data
output_data = dict()
dir_list = []
file_list = set()
for dirpath, dirnames, files in os.walk(target):
    if dirpath not in dir_list:
        dir_list.append(dirpath)
        output_data[dirpath] = []
    for f in files:
        file_list.add(f)
        output_data[dirpath].append(f)

# Write data to text files per folder
for dir in dir_list:
    dir_files = output_data[dir]
    if len(dir_files) > 0:
        print(dir.split('\\')[-1])
        file_name_p1 = dir.split('\\')[-1]
        file_name = file_name_p1 + ".txt"
        if os.path.isfile(str(os.getcwd()[0]) + "\\" + file_name):
            print("ERROR: Duplicate subdirectory names. (" + file_name + ")")
        with open(file_name, 'w') as f:
            f.write(dir + "\n")
            for file in dir_files:
                if file[0].isalpha():
                    f.write(file + "\n")
            f.close()