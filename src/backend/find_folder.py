import os
import operations

def find_folder(start_dir='/', folder_name='Images'):
    # Search local directories
    for root, dirs, files in os.walk(start_dir):
        for dir in dirs:
            if dir == folder_name:
                folder_path = os.path.join(root, dir)
                return folder_path
    
    # Search USB devices
    volumes = [f"/Volumes/{d}" for d in os.listdir("/Volumes") if not d.startswith('.')]
    for volume in volumes:
        for root, dirs, files in os.walk(volume):
            if folder_name in dirs:
                folder_path = os.path.join(root, folder_name)
                return folder_path