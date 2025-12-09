from operations import *
from utilities import *

def commands(command):
    if command == "--help":
        print("gitfile --sync: Copies all data from a remote repository into an empty folder. Two-way syncing may be enabled. \n")
    elif command == "--sync":
        message = sync()
        print(message)
    elif command == "--testfinder":
        file_path = testFinder()
        print("You picked:", file_path)
    elif command == "--testimage":
        image_path = testImage()
        print("You picked:", image_path)