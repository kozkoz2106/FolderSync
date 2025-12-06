from utilities import *
import os
from find_folder import *

# HELPER FUNCTIONS
def syncOneWay(source_list, destinationDIR, destinationDIR_name):
    for item in source_list: 
        copytree(item, destinationDIR, dirs_exist_ok=True)

    return "The contents of have been copied into " + destinationDIR_name + "."

def syncBothWay(sourceDIR, destinationDIR, source_list, destinationDIR_name):
    copytree(sourceDIR, destinationDIR, True)
    copytree(destinationDIR, sourceDIR, True)
    return "The contents of " + sourceDIR_name + " and " + destinationDIR_name + " have been synced both ways."

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

    sync_type = input("Two way syncing? Type 'yes' or 'no': ")

    while sync_type != 'yes' and sync_type != 'no':
        sync_type = input("Not a valid command. Type 'yes' or 'no': ")
    
    if sync_type == 'no':
        return syncOneWay(source_list, destinationDIR, destinationDIR_name)
    elif sync_type == 'yes':
        return syncBothWay(source_list, destinationDIR, destinationDIR_name)