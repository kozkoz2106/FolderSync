from .utilities import *
import subprocess
from PIL import Image

from .utilities import compare_hash

class SyncOperations:
    source_list = []
    dest_list = []

    def syncFiles(self, source_list, dest_list, one_way):
        for source in source_list: 
            for dest in dest_list:
                copytree(source, dest, dirs_exist_ok=True)
        if one_way == False:
            return "The contents of your source(s) have been copied into your destination(s)"
        else:  
            for source in source_list:
                for dest in dest_list:
                    copytree(dest, source, dirs_exist_ok=True)
            for source in source_list:
                for dest in dest_list:
                    copytree(source, dest, dirs_exist_ok=True)
            return "The contents of your source(s) and destination(s) have been synced both ways."

    def terminal_sync(self):
        print("Enter a source folder(s): ")
        source_list = self.selectFolders()

        print("Enter a destination folder: ")
        dest_list = self.selectFolders()

        if not (source_list and  dest_list):
            return "Nothing was selected"

        one_way = False
        sync_type = input("Two way syncing? Type 'yes' or 'no': ")

        while sync_type != 'yes' and sync_type != 'no':
            sync_type = input("Not a valid command. Type 'yes' or 'no': ")
        
        if sync_type == 'yes':
            one_way = True

        return self.syncFiles(source_list, dest_list, one_way)

    def selectFolders(self):
        script = '''
        set theFolders to choose folder with multiple selections allowed
        set output to ""
        repeat with f in theFolders
            set output to output & (POSIX path of f) & linefeed
        end repeat
        return output
        '''
        
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )

        return [line for line in result.stdout.splitlines() if line.strip()]

    def compHash(self):
        return compare_hash()

    def select_src(self):
        source_list = self.selectFolders()
        return source_list

    def select_dst(self):
        dest_list = self.selectFolders()
        return dest_list


