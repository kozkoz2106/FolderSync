import shutil
import os
#import subprocess
#import pyusb
#from tkinter import *
from find_folder import *

#def find_folder_external(start_dir='/', folder_name ='Images'):
   # return 0

# def find_folder_local(start_dir='/', folder_name='Images'):
#     for root, dirs, files in os.walk(start_dir):
#         for dir in dirs:
#             if dir == folder_name:
#                 full_path = os.path.join(root, dir)
#                 try:
#                     print(full_path)
#                     return full_path
                
#                 except Exception as e:
#                     print(f"Error opening {full_path}: {e}")
                    
    #find_folder_external('/Volumes', folder_name)

def clone():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")
    sourceDIR = find_folder_local('/Users/aarohpurani/', source)
    destinationDIR = find_folder_local('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name

def push():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")
    sourceDIR = find_folder_local('/Users/aarohpurani/', source)
    destinationDIR = find_folder_local('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))
    
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    