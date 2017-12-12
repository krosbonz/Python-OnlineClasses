#Finding something in the content of a line

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >=0:
        print(line)

#Is the same as 

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)


#Using regular expressions to find a line that starts with a character

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

#Is the same as 

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)


#The dot and asterisk 
^X.*:

###This will find lines that start with "X" then have any number of characters 
#(even whitespace) and then a colon. The X and the colon are not special characters.

^X-\S+:

###This will find a line that starts with "X-" followed by any non-whitespace characters (\S), 
#one or more characters (+), followed by a colon

