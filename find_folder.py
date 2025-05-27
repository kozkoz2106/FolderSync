import os

# def find_folder_external(start_dir='/', folder_name ='Images'):
#     return 0

def find_folder_local(start_dir='/', folder_name='Images'):
    for root, dirs, files in os.walk(start_dir):
        for dir in dirs:
            if dir == folder_name:
                full_path = os.path.join(root, dir)
                try:
                    return full_path
                except Exception as e:
                    print(f"Error opening {full_path}: {e}")
                    
    #find_folder_external('/Volumes', folder_name)