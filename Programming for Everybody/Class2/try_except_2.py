fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ')
    quit()

count = 0
for line in fhand:
    if line.startwith('Subject:'):
        count = count + 1
print('There were', count, 'subject line in', fname)

