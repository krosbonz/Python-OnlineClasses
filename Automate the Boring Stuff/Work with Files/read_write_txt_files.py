# Opening a file for read and write

# NOTE: You need a "\" to escape backslashes

open_file = open('c:\\users\\hauck\\desktop\\temp.txt')
content = open_file.read()
print(content)

# Close an open file
open_file.close()


open_file = open('c:\\users\\hauck\\desktop\\temp.txt')
open_file.readlines()
# Output
['Hello world!\n', "What's a happening?!"]
# Each line is a list in a string


# Open file in Write or Append mode
open_file = open('c:\\users\\hauck\\desktop\\temp.txt', 'w')
# Opening in write mode will overight an existing file, or create a new file
# if one doesn't exist

open_file = open('c:\\users\\hauck\\desktop\\temp.txt', 'a')
# Opening in append mode will append strings to an existing file or
# create a new file if it doesn't exist

# NOTE: If file doesn't exist 'w' and 'a' will create the file

# Full process to append and then output what is in the file;
open_file = open('c:\\users\\hauck\\desktop\\temp.txt', 'a')
open_file.write('stuff and stuff')
open_file.close()

# Either
open_file.readlines()
# Output
# [blahblahblah..., per line...]

# Or
open_file.read()
# Output
blahblahblah
newline... etc...

# Shelve - Store non-text information to a file. Use like dictionary
import shelve

shelffile = shelve.open('mydata')
shelffile['cats'] = ['fred', 'ginger', 'harry', 'tabby']
shelffile.close()

shelffile = shelve.open('mydata')
shelffile['cats']
# Output
['fred', 'ginger', 'harry', 'tabby']

# Shelve allows you to call key / value like dictionary
shelffile.open('mydata')
shelffile.keys()
list(shelffile.keys())
# Output
['cats']
list(shelffile.values())
# Output
[['fred', 'ginger', 'harry', 'tabby']]










