import shutil
import os
import subprocess

def find_folder(start_dir='/', folder_name='example.txt'):
    for root, dirs, files in os.walk(start_dir):
        for dir in dirs:
            if dir == folder_name:
                full_path = os.path.join(root, dir)
                try:
                    subprocess.run(['open', full_path])
                    return 
                except Exception as e:
                    print(f"Error opening {full_path}: {e}")

def clone():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")

    sourceDIR = "/Users/aarohpurani/git-files/test folders/pcFolder"
    destinationDIR = "/Users/aarohpurani/git-files/test folders/usbFolder"   

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of" + sourceDIR_name + " have been copied into " + destinationDIR_name

def push():
    source = input("Enter a source folder \n")
    destination = input("Enter a destination folder\n")
    sourceDIR = "/Users/aarohpurani/git-files/test folders/usbFolder"
    destinationDIR = "/Users/aarohpurani/git-files/test folders/pcFolder"

    sourceDIR_name = (os.path.basename(sourceDIR))
    destinationDIR_name = (os.path.basename(destinationDIR))
    
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    