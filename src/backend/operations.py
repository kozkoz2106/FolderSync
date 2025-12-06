from utilities import *
import os
from find_folder import *

# HELPER FUNCTIONS
def syncFiles(source_list, destinationDIR, destinationDIR_name, one_way):
    for item in source_list: 
        copytree(item, destinationDIR, dirs_exist_ok=True)
    if one_way == False:
        return "The contents of your sources have been copied into " + destinationDIR_name + "."
    else:  
        for item in source_list:
            copytree(destinationDIR, item, dirs_exist_ok=True)
        return "The contents of your sources and " + destinationDIR_name + " have been synced both ways."

# PRIMARY FUNCTIONS
def sync():

    home_path = os.path.expanduser("~")
    source_list = []

    print("Enter a source folder(s): ")

    while (input != 'done'):
        source = input()
        if source == 'done':
            break
        sourceDIR = find_folder(home_path, source)
        if sourceDIR == 'not found':
            print('Folder ' + source + ' not found')
        else:
            print(source + ' selected')
            source_list.append(sourceDIR)

    destination = input("Enter a destination folder: ")
    destinationDIR = find_folder(home_path, destination)

    if destinationDIR == 'not found':
        print('Folder ' + destination + ' not found')
        exit(0)
    destinationDIR_name = (os.path.basename(destinationDIR))

    one_way = False
    sync_type = input("Two way syncing? Type 'yes' or 'no': ")

    while sync_type != 'yes' and sync_type != 'no':
        sync_type = input("Not a valid command. Type 'yes' or 'no': ")
    
    if sync_type == 'no':
        return syncFiles(source_list, destinationDIR, destinationDIR_name, one_way)
    else:
        one_way = True
        return syncFiles(source_list, destinationDIR, destinationDIR_name, one_way)