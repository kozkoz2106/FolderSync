from dataclasses import dataclass
from response import commands
import json

# File pull (copy all data), File push (push data to create new), File merge (integrate changes), File clone (clone file)
# Each folder has a designated #pull and #push. Designated by a folder that contains a hash bonding it to another folder, 
# denoting it as either the remote or the local. 

input = input().split(' ', maxsplit=2)
file = input[0]
command = input[1]

if file != 'gitfile' :
    print(file + " is not a valid command. See 'gitfile --help'.")
    exit(0)
    
commands(command)