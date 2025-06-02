import shutil
import os
from find_folder import *

# HELPER FUNCTIONS
def syncOneWay(sourceDIR, destinationDIR, sourceDIR_name, destinationDIR_name):
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " have been copied into " + destinationDIR_name + "."

def syncBothWay(sourceDIR, destinationDIR, sourceDIR_name, destinationDIR_name):
    shutil.copytree(sourceDIR, destinationDIR, dirs_exist_ok=True)
    shutil.copytree(destinationDIR, sourceDIR, dirs_exist_ok=True)
    return "The contents of " + sourceDIR_name + " and " + destinationDIR_name + " have been synced both ways."

# PRIMARY FUNCTIONS
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

    sync_type = input("Two way syncing? Type 'yes' or 'no': ")

    while sync_type != 'yes' and sync_type != 'no':
        sync_type = input("Not a valid command. Type 'yes' or 'no': ")
    
    if sync_type == 'no':
        return syncOneWay(sourceDIR, destinationDIR, sourceDIR_name, destinationDIR_name)
    elif sync_type == 'yes':
        return syncBothWay(sourceDIR, destinationDIR, sourceDIR_name, destinationDIR_name)