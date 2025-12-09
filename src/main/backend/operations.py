from utilities import *
import os
import subprocess
from PIL import Image

from utilities import compare_hash

def syncFiles(source_list, dest_list, one_way):
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

def sync():
    source_list = []
    dest_list = []

    print("Enter a source folder(s): ")
    source_list = selectFolders()

    print("Enter a destination folder: ")
    dest_list = selectFolders()

    one_way = False
    sync_type = input("Two way syncing? Type 'yes' or 'no': ")

    while sync_type != 'yes' and sync_type != 'no':
        sync_type = input("Not a valid command. Type 'yes' or 'no': ")
    
    if sync_type == 'yes':
        one_way = True

    return syncFiles(source_list, dest_list, one_way)

def selectFolders():
    script = '''
    set theFolders to choose folder with multiple selections allowed
    set output to ""
    repeat with f in theFolders
        set output to output & (POSIX path of f) & linefeed
    end repeat
    return output
    '''
    
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )

    return [line for line in result.stdout.splitlines() if line.strip()]

def compHash():
    return compare_hash()