#%% To find strings to be extracted we use "re.findall()"

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+' ,x)
num = float(y[0])
print(y)

#%% Output - List of strings consisting if digits
['2', '19', '42']

#[0-9] indicates looking for a single digit, and "+" indicates looking for one or more
#[AEIOU] = Any capitalized letter
#%%

#%% Greedy matching
import re
x = 'From: Using the  : character'
y = re.findall('^F.+:' ,x)
print(y)
#%% Output
['From: Using the  :']

#%% Greedy matching II
y = 'From stephen.marquerd@uct.ac.za Sat Jan 5 09:14:16 2008'
x = re.findall('\S+@\S+' ,y)
print(x)
#%% Output
['stephen.marquerd@uct.ac.za']


#%% Non-greedy matching
import re
x = 'From: Using the  : character'
y = re.findall('^F.+?:' ,x)
print(y)

#%% Output - Only goes to the first instance of what is being searched
['From:']

#%% Additional requirements to find, but limit output
y = 'From stephen.marquerd@uct.ac.za Sat Jan 5 09:14:16 2008'
x = re.findall('^From (\S+@\S+)' ,y)
print(x)

#%% Output - Looks for lines that start with "From", but extracts only the email address
['stephen.marquerd@uct.ac.za']

#Another option
x = re.findall('^From .*@([^ ]*)' ,y)
#This says look for lines that start with "From and have any number of characters up to "@"
#extract all non blank characters after "@"