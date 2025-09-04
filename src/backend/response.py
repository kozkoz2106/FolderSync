from operations import *

def commands(command):
    if command == "--help":
        print("gitfile --sync: Copies all data from a remote repository into an empty folder\ngitfile --pull [folder]: Updates local repository with changes from remote repository \n")
    elif command == "--sync":
        message = sync()
        print(message)

