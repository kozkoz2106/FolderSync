from operations import *
from utilities import *

def commands(command):
    message = ""
    if command == "--help":
        message = ("gitfile --sync: Copies all data from a remote repository into an empty folder. Two-way syncing can be enabled \n" 
                  "gitfile --merge: Merges selected folders into a single, new folder. \n")
        print(message)
    elif command == "--sync":
        message = sync()
        print(message)
    elif command == "--merge":
        message = merge()
        print(message)
    elif command == "--comparehash":
        hash = compHash()
        if hash == True:
            print("The files are identical.")
        else:
            print("The files are different.")