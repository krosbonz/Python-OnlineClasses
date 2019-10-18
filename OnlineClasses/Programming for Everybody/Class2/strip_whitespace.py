#Strip Whitespace
#lstrip() , rstrip(), strip() - Strips whitespace from left, right or all

greet = '   Hello Bob'
zip = greet.lstrip()
print(zip)

#The space between "Hello" and "Bob" will remain

#Opening a file, finding specific lines and stripping whitespace to keep from seeing extra blank lines
nfile = open(something.txt)
for i in nfile:
    i = i.rstrip()
    if i.startswith('From'):
        print(i)