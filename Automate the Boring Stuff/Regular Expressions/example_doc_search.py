import re pyperclip
# pyperclip > allows the copy and paste functionality

phone_regex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? # Area code
# The pipe indicates "or". The area code can be just three digits "603"
# or in brackets "(603)". The brackets are escaped with "\".
# The area code is in a group, and it is optional, so it is followed by a "?" 
# which means zero or one times
(\s|-) # After the area code there could either be a space or a dash separator
\d\d\d # First three digits in ph num
-      # Second separator
\d\d\d\d\      # Last four digits in ph num
((ext(\.)?\s|x)# Extension starts with "ext", maybe followed by a period, followed 
               # by a space OR it is just the letter "x". That is in a group with 
               # the actual ext.
(\d{2,5}))?  # The actual extension 2 to 5 digits. And the ext is optional.
)            # See the note below for why the entire function is in one big group
''', re.VERBOSE)

email_regex = re.compile(r'''
[a-zA-Z._+]+  # All information in front of "@" one or more char
@             # @ symbol
[a-zA-Z._+]+  # Domain information
''', re.VERBOSE)

textinfo = pyperclip.paste()
# this will paste the full text from an open file into a variable

find_phone_regex = phone_regex.findall(textinfo)
find_email_regex = email_regex.findall(textinfo)

# NOTE: In class the "phone_regex" part created a very messy list of tuples because
# when using "findall" each group is put in its own tuple. To deal with this the
# instructor put the entire "phone_regex" function in one big group. 

# Once extracted you can loop over the information
all_phone_nums = []
for x in find_phone_regex:
    all_phone_nums.append(x[0])
# The "[0]" will grab just the first string in the tuple

# Once all of the numbers is in the all_phone list we can put each one on its
# own line for readability
results = '\n'.join(all_phone_nums) + '\n' + '\n'.join(find_email_regex)

# Finally, copy the final output to the clipboard
pyperclip.copy(results)

