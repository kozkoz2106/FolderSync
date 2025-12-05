from operations import *
import shutil

def commands(command):
    if command == "--help":
        print("gitfile --sync: Copies all data from a remote repository into an empty folder. Two-way syncing may be enabled. \n")
    elif command == "--sync":
        message = sync()
        print(message)
    elif command == "--print":
        print(shutil.__file__)
