#%%Using "re.search()" returns a True/False depending on if the string matches the reg expression

#This is the same as...
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >=0:
        print(line)

#%% This 
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)


#%% Using regular expressions to find a line that starts with a character

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

#%%Is the same as 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):
        print(line)


#%%The dot and asterisk 
^X.*:

#This will find lines that start with "X" then a charactger (.) zero or more times (*) 
#(including whitespace) and then a colon. The X and the colon are not special characters

^X-\S+:
#%%This will find a line that starts with "X-" then a non-whitespace character (\S) one or more times (+), followed by a colon

