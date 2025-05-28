import shutil
import os
#import subprocess
#import pyusb
#from tkinter import *
from find_folder import *

def clone():
    source = input("Enter a source folder: ")
    destination = input("Enter a destination folder: ")
    sourceDIR = find_folder_local('/Users/aarohpurani/', source)
    destinationDIR = find_folder_local('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name

def push():
    source = input("Enter a source folder: ")
    destination = input("Enter a destination folder: ")
    sourceDIR = find_folder_local('/Users/aarohpurani/', source)
    destinationDIR = find_folder_local('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))
    
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    