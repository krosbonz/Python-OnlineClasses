#Prompt for file input, open, print entire file in uppercase, removing extra line breaks
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
chr = fh.read().upper().strip()
print(chr[:])