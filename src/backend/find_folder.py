import os

def find_folder(start_dir='/', folder_name='Images'):
    for root, dirs, files in os.walk(start_dir):
        for dir in dirs:
            if dir == folder_name:
                full_path = os.path.join(root, dir)
                return full_path
    # for root, dirs    