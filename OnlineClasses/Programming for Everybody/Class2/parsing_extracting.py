Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

#This returns the position in the string where the "@" is located  - 21
atpos = data.find('@')
print(atpos)

# The ".find" parameter will take a second argument "start from here". 
# So, "sppos" is looking for a space starting from the "atpos" or position 21 
sppos = data.find(' ',atpos)
print(sppos)

#We now want to capture everything from after the "@" (position 21) until the first space after the "@"
place = data[atpos+1 : sppos]
print(place)

#Output is "uct.ac.za"
