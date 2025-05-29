import shutil
import os
from find_folder import *

not_found = 'Folder not found'

def sync():
    source = input("Enter a source folder: ")
    sourceDIR = find_folder('/Users/aarohpurani/', source)
    if sourceDIR == 'not found':
        print('Folder ' + source + ' not found')
        exit(0)
    sourceDIR_name = (os.path.basename(sourceDIR))

    destination = input("Enter a destination folder: ")
    destinationDIR = find_folder('/Users/aarohpurani/', destination)
    if destinationDIR == 'not found':
        print('Folder ' + destination + ' not found')
        exit(0)
    destinationDIR_name = (os.path.basename(destinationDIR))

    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name
    