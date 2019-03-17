# From the Python shell in Windows you have two choices for using paths

# c:\\users\\hauck
# or
# r'c:\users\hauck'

# NOTE: Backslashes "\" require being escaped with another backslash 

# To make your code usable with all operating systems, you import
# the "os" module
import os

os.path.join('folder1', 'folder2', 'folder3', 'file.doc')
# Output
'folder1\\folder2\\folder3\\file.doc'

# Current working directory
os.getcwd()
# Output
'C:\\Users\\hauck\\OneDrive\\Documents\\VS Projects\\Python\\Python-OnlineClasses'

# To change the CWD
os.chdir('c:\\users\\hauck')

# Dot location
# . = This folder
# .. = The parent folder

# .\ - This folder
# ..\ - Root folder

# Absolute paths
os.path.abspath('stuff.png')
# This assumes the file is in the CWD
# Output
'c:\\users\\hauck\\stuff.png'
os.path.abspath('..\\..\\stuff.png')
# You are telling Python the parent folder's parent folder contains stuff.png

# Is absolute path - To confirm the path is an abs path
os.path.isabs('\\folder\\folder\\stuff.png')
# Output
True
os.path.isabs('..\\..\\stuff.png')
# Output
False

# Get directory name or file name
os.path.dirname('c:\\folder1\\folder2\stuff.png')
# Output
'c:\\folder1\\folder2' # Returns just the path minus the file

os.path.basename('c:\\folder1\\folder2\stuff.png')
# Output
'stuff.png' # Returns just the last folder\file in the path
os.path.basename('c:\\folder1\\folder2')
# Output
'folder2'

# Does path exist
os.path.exists('c:\\folder1\\folder2\\stuff.png')
False
# Does the file exist in the path
os.path.isfile('c:\\users\\hauck\\.gitconfig')
True
# Does the folder exist
os.path.isdir('c:\\users\\hauck')
True

# Size of file
os.path.getsize('c:\\users\\hauck\.gitconfig')
# Returns size in bytes

# Return list of files in a folder
os.listdir('c:\\users\\hauck')
# Output
['.android', '.bash_history', '.gitconfig', etc...]

# Make a new directory
os.makedirs('c:\\stuff\\yomama')