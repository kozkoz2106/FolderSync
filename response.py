import sys, os
from fileopps import *

def commands(command):
    if command == "--help":
        print("gitfile --clone: Copies all data from a remote repository into an empty folder\ngitfile --pull [folder]: Updates local repository with changes from remote repository \n")
    elif command == "--clone":
        message = clone()
        print(message)
    #elif command == "Pull files":
        
    #elif command == "Push files":
    elif command == "--push":
        message = push()
        print(message)
    
    elif command == "--find_folder":
        find_folder('/Users/aarohpurani', 'brainrot')

    #elif command == "Merge files":

