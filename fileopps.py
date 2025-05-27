import shutil
import os
import subprocess
#from tkinter import *

def find_folder(start_dir='/', folder_name='Images'):
    print("a")
    for root, dirs, files in os.walk(start_dir):
        print('b')
        for dir in dirs:
            print('c')
            if dir == folder_name:
                print('d')
                full_path = os.path.join(root, dir)
                try:
                    print('e')
                    print(full_path + folder_name)
                    subprocess.run(['open', full_path])
                    return 
                except Exception as e:
                    print('f')
                    print(f"Error opening {full_path}: {e}")

def clone():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")

    sourceDIR = "/Users/aarohpurani/Desktop/Images/pc"
    destinationDIR = "/Users/aarohpurani/Desktop/Images/usb"   

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name

def push():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")
    sourceDIR = "/Users/aarohpurani/Desktop/Images/test2"
    destinationDIR = "/Users/aarohpurani/Desktop/Images/test1"

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))
    
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    