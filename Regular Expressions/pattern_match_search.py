
import re
# Contains all of the regular expression functions

# Pattern Match

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# "\d" stands for any numeric digit
phone_regex.search('my number is 405-456-2365')

# Output
<_sre.SRE_Match object; span=(13, 25), match='405-456-2365'>
# Returns a Match Object


# So tie the MO to a variable
mo = phone_regex.search('my number is 405-456-2365')
mo.group()
# Group - will return the entire pattern
'405-456-2365'

# If you are looking to only capture a portion of the pattern, 
# you can break the pattern into groups
import re

phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_regex.search('my number is 405-456-2365')
mo.group(1)
# Output
'405'

# To escape the bracket character instead of breaking it
# into a group
phone_regex = re.compile(r'\(\d\d\d)-\d\d\d-\d\d\d\d')
mo = phone_regex.search('my number is (405) 456-2365')
# Output
'(405) 456-2365'


# Pipe
import re

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('I bet the Batmobile goes real fast')
mo.group()

mo.group(1)
# This will return the matching string
# Output
'mobile'


# Using wild cards
# ? - Optional - Zero or one time
# * - Optional - Zero or more times
# + - Not optional - Must appear one or more times

bat_regex = re.compile(r'Bat(wo)?man')
# This will find "Batman" or "Batwoman"
# The "?" indicates "wo" can be found zero or one times (not more)


# Combining the digital phone pattern with the optional inclusion
phone_regex = re.compile('r (\d\d\d-)?\d\d\d-\d\d\d\d')
# This will find ph numbers either with or without the area code

# NOTE: if you actually need to look for a any wildcard punctuation you can
# escape the "?,*,+" with a backslash in front of it "\?"
# re.copile('r'dinner\?')

re.compile('r (\+\*\?)+')
# This group must appear one or more times

# Look for a string a certain number of times
re.compile('r "ha" {3}')
# Look for a string with "hahaha"

re.compile('r ((\d\d\d-)?\d\d\d-\d\d\d\d(,)?) {3}')
# Look for a string with three phone numbers which may or may not
# have area codes and which may or may not be separated by a ","

# Match a range of repititions
re.compile('r (ha) {3,5})
# Between three and five times
re.compile('r (ha) {,5})
# Up to five times
re.compile('r (ha) {3,})
# At least three times

# Greedy match
dig_regex = re.compile(r'\d {3,5}')
dig_regex.search('12345678')
# This would return five numbers because by default Python takes the higher amount

# Non-greedy match 
 dig_regex = re.compile(r'\d {3,5}?')
# This would return a non-greedy, or shortest string possible

