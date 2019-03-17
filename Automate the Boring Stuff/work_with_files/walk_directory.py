import os

for folders, subfolders, files in os.walk('c:\\Users\\hauck\\desktop\\stuff'):
    print('The Folder name is ' + folders)
    print('The Subfolders in ' + folders + 'are: ' + str(subfolders))
    print('List of files in' + folders + 'are: ' + str(files))
    print()

# Output
The Folder name is c:\Users\hauck\desktop\stuff
The Subfolders in c: \Users\hauck\desktop\stuffare:['regular_expressions', 'work_with_files']
List of files inc:\Users\hauck\desktop\stuffare: []

The Folder name is c:\Users\hauck\desktop\stuff\regular_expressions
The Subfolders in c:\Users\hauck\desktop\stuff\regular_expressionsare: []
List of files inc: \Users\hauck\desktop\stuff\regular_expressionsare:['char_class.py', etc...]

The Folder name is c:\Users\hauck\desktop\stuff\work_with_files
The Subfolders in c:\Users\hauck\desktop\stuff\work_with_filesare: []
List of files inc:\Users\hauck\desktop\stuff\work_with_filesare: ['absolute_rel_paths.py', etc...]

# Then you can use a loop to remove directories or files

for folder in folders:
    if 'foldername' in folder:
        os.rmdir(folder)

