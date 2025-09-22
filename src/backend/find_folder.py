import os

def find_folder(start_dir='/', folder_name='Images'):
    # Search local directories
    for root, dirs, files in os.walk(start_dir):
        for dir in dirs:
            if dir == folder_name:
                return os.path.join(root, dir)
    
    # Search USB devices
    volumes = [f"/Volumes/{d}" for d in os.listdir("/Volumes") if not d.startswith('.')]
    for volume in volumes:
        for root, dirs, files in os.walk(volume):
            if folder_name in dirs:
                return os.path.join(root, folder_name)
            
    return 'not found'
