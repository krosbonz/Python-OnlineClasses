#%% The correct answer
import re

hand = open('regex_sum_40848.txt')
numtot = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for i in stuff:
        numtot = numtot + int(i)
print(numtot)

#%%That is much easier than this mess

import re
hand = open('sample2.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        nos = re.findall('[0-9]+', word)
        for i in nos:
            nmb = int(i)
            numlist.append(nmb)
print(sum(numlist))            