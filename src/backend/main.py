from dataclasses import dataclass
from response import commands

# File pull (copy all data), File push (push data to create new), File merge (integrate changes), File clone (clone file)
# Each folder has a designated #pull and #push. Designated by a folder that contains a hash bonding it to another folder, 
# denoting it as either the remote or the local. 

input = input().split(' ', maxsplit=2)
file = input[0]
if file == 'quit':
    exit(0)
elif file != 'gitfile' :
    print(file + " is not a valid command. See 'gitfile --help'.")
    exit(0)b
elif len(input) != 2:
    print('Two arguments are needed: "gitfile" and a command.')
else:
    command = input[1]
    commands(command)