from utilities import *
import os
from find_folder import *

# HELPER FUNCTIONS
def syncFiles(source_list, dest_list, one_way):
    print('a')
    for source in source_list: 
        for dest in dest_list:
            copytree(source, dest, dirs_exist_ok=True)
    if one_way == False:
        return "The contents of your source(s) have been copied into your destination(s)"
    else:  
        for source in source_list:
            for dest in dest_list:
                copytree(dest, source, dirs_exist_ok=True)
        for source in source_list:
            for dest in dest_list:
                copytree(source, dest, dirs_exist_ok=True)
        return "The contents of your source(s) and destination(s) have been synced both ways."

# PRIMARY FUNCTIONS
def sync():

    home_path = os.path.expanduser("~")
    source_list = []
    dest_list = []

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

    print("Enter a destination folder: ")

    while (input != 'done'):
        print('a')
        dest = input()
        if dest == 'done':
            break
        destDIR = find_folder(home_path, dest)
        if destDIR == 'not found':
            print('b')
            print('Folder ' + dest + ' not found')
        else:
            print('c')
            print(dest + ' selected')
            dest_list.append(destDIR)
        print('d')

    one_way = False
    sync_type = input("Two way syncing? Type 'yes' or 'no': ")

    while sync_type != 'yes' and sync_type != 'no':
        sync_type = input("Not a valid command. Type 'yes' or 'no': ")
    
    if sync_type == 'no':
        return syncFiles(source_list, dest_list, one_way)
    else:
        one_way = True
        return syncFiles(source_list, dest_list, one_way)
    