# Shell Utility module allows copying and moving of files

import shutil
# Copy a file
shutil.copy('c:\\users\\hauck\\desktop\\temp.txt', 'c:\\users\\hauck\\documents')
# Or to copy and rename
shutil.copy('c:\\users\\hauck\\desktop\\temp.txt', 'c:\\users\\hauck\\desktop\\perm.txt')
# Move a file
shutil.copy('c:\\users\\hauck\\desktop\\temp.txt', 'c:\\stuff')
# Rename a file in place
shutil.copy('c:\\users\\hauck\\desktop\\temp.txt', 'c:\\users\\hauck\\desktop\\perm.txt')

# Copy files and folders
shutil.copytree('c:\\users\\hauck', 'c:\\users\\smith')


# Delte files / folders
import os

os.unlink('c:\\somefile\\somewhere\\stuff.txt')
# Delete folder
os.rmdir('c:\\somefolder')
# NOTE: Using this command a folder needs to be empty to delete it

# Delete a folder and all subfolders and files
import shutil
shutil.rmtree('c:\\somefolder')

# Import, change dir, delete files with specific ext
import shutil
import os

os.chdir('c:\\stuff\\substuff')

for files in os.listdir():
    if files.endswith('.txt'):
        os.unlink(files)
        print(files)
        
# NOTE: Better idea than deleting a file is to install send2trash module
# pip install send2trash
# Instead of perm delete, will send to recyclebin

import send2trash
send2trash.send2trash(files)



