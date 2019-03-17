import re

secret_agent = 'Agent Steve is giving secret documents to Agent Betty.'

names_regex = re.compile(r'Agent \w+')
names_regex.findall(secret_agent)
# Output
['Agent Steve', 'Agent Betty']

names_regex.sub('REDACTED', secret_agent)
# Notice that "sub" replaces "findall"
# This replaces the string pattern being searced with the replacement string

# Output
'REDACTED is giving secret documents to REDACTED.'

# Replace only part of a word
names_regex = re.compile(r'Agent (\w)\w*')
# Find "Agent", space, then a char followed by any number of characters
# and put the first letter in group1

names_regex.sub(r'Agent \1****', secret_agent)
# Replace the agent name with the string found in group1 followed by "****"
# Output
'Agent S**** is giving secret documents to Agent B****.'


# Verbose mode eliminates white space for ease of reading code

re.compile(r'''
\d\d\d # Area code
-      # Dash blah blah blah...
\d\d\d
-
\d\d\d\d
''', re.VERBOSE)