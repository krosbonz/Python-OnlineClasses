#Open file with r = read or w = write
nfile = open(somefile.txt,r)

#When a for loop is run against a file it runs one time for each LINE in the file
for i in nfile:
    print(i)

#Count the lines
count = 0
for i in nfile:
    count = count + 1
print("There are: ",count, "lines")

#To get a count of characters in the file
nfile = open(somefile.txt,r)
chr = nfile.read()
print(len(chr))
#Output - some number of characters in the file

#You can also slice with this command
nfile = open(somefile.txt,r)
chr = nfile.read()
print(chr[:20])
#Output - The first 20 characters from the file

#Using the "startswith" method
nfile = open(somefile.txt)
for i in nfile:
    if i.startswith('From:'):
        print(line)

#Opening a file, finding specific lines and stripping whitespace to keep from seeing extra blank lines
nfile = open(something.txt)
for i in nfile:
    i = i.rstrip()
    if i.startswith('From'):
        print(i)


#This will produce the same output, but will skip all lines that don't start with "From
nfile = open(something.txt)
for i in nfile:
    i = i.rstrip()
    if not i.startswith('From'):
        continue
    print(i)


#All of these functions will work by prompting for filename
ofile = input("What is the file name: ")
nfile = open(ofile)
for i in nfile:
    i = i.rstrip()
    if i.startswith('From'):
        print(i)