import shutil
import os
#import subprocess
#import pyusb
from find_folder import *

not_found = 'Folder not found'

def clone():
    source = input("Enter a source folder: ")
    destination = input("Enter a destination folder: ")
    sourceDIR = find_folder('/Users/aarohpurani/', source)
    destinationDIR = find_folder('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    #if (sourceDIR_name == )
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name

def push():
    source = input("Enter a source folder: ")
    destination = input("Enter a destination folder: ")
    sourceDIR = find_folder('/Users/aarohpurani/', source)
    destinationDIR = find_folder('/Users/aarohpurani/', destination)

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))
    
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    