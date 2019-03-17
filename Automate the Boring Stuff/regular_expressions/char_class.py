# Character classes
# \d - Any numeric digit 0-9
# \D - Any character that is not a numeric digit from 0-9
# \w - Any letter, numeric digit or underscore character - Used to find words
# \W - Any character not a letter, numeric digit or underscore
# \s - Any space, tab, newline char - Used to match space characters
# \S - Any char not a space, tab, newline

# Using wild cards
# ? - Optional - Zero or one time
# * - Optional - Zero or more times
# + - Not optional - Must appear one or more times
# . - Any single character
# .* - Any number of any characters
# .*? - Any number of any characters non-greedy (finds only first instance)

# Include all characters INCLUDING "\n" newline
newline_regex = re.compile(r'.*', re.DOTALL)

# Ignore capitalization
caps_regex = re.compile(r'.*', re.I) 
# This can also be "re.IGNORECASE"

# You can also use multiple options with pipe
regex = re.compile(r'.*', re.DOTALL | re.VERBOSE | re.IGNORECASE)



import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords leaping, 9 ladies dancing'

song_regex = re.compile(r'\d+\s\w+')
# Search for at least one digit, exactly one space and at least one word
# ('r\d+ \w+) - This would work as well for the space 

song_regex.findall(lyrics)
# Output
['12 drummers', '11 pipers', '10 lords', '9 ladies']


# Make your own character class
regexObj = re.compile(r'[]')
# Whatever you place in the brackets will be the searched items
[a-f]
[a-fA-F]
[aeiouAEIOU]
# This will find ALL vowels and put them in a list
(r'[aeiouAEIOU] {2}')
# This will find double vowels "00" or "ae"
[^aeiou]
# This is a Negative Character Class. It will find everything that is NOT a vowel


# Searching at the beginning of a string with "^"
begin_with_regex = re.compile(r'^Hello')
# This will only find the word "Hello" at the beginning of a string

# Searching at the end of a string with a "$"
end_with_regex = re.compile(r'Hello$')

# Search for string that has a specific pattern throughout
begin_end_regex = re.compile(r'^/d$')
# Will find - 123457654
# Will not find - 123T0987 < There is a "T" in the middle of the string

# Search using the "." > Return one of ANY character (including space, punct, etc...)
dot_regex = re.compile(r'.at')
dot_regex.findall('The cat in the hat just spat on the mat')
# Output
['cat', 'hat', 'pat', 'mat']
# Notice "pat" was returned and not "spat"

dot_regex = re.compile(r'.{1,2}at')
dot_regex.findall('The cat in the hat just spat on the mat')
# This says we are looking for "at" preceeded by one or two of any character
# Output
[' cat', ' hat', 'spat', ' mat']
# Notice there is now a space for each item except "spat", because
# it looks for one or two of ANY character before "at"

# Search using the ".*" > Find all of any character EXCEPT new line character "\n"
'First Name: Steve Last Name: Charles'
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
# This will look for the "First...:" then a space, then any num of characters
# then "Last...:" then a space, then any num of characters
name_regex.findall('First Name: Steve Last Name: Charles')
# Output
[('Steve', 'Charles')]


# Greedy vs Non-greedy 
serve = '<To serve humans> for dinner>'
nongreedy_regex = re.compile(r'<(.*?)>')
nongreedy_regex.findall(serve)
# Output
['To serve humans']

greedy_regex = re.compile(r'<(.*)>')
# Output
['To serve humans> for dinner']

