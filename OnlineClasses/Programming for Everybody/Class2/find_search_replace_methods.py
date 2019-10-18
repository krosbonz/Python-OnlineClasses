Find
# returns the string position (location) where the first 'na' is located
fruit = 'banana'
pos = fruit.find('na')
print(pos)
# Returns - 2
# If you try to "find" something that doesn't exist it returns -1

Replace
#Replace takes the first entry is what is being replaced with the second entry
fruit = 'banana'
fez = fruit.replace('b', 't')
print(fez)
#Returns - "tanana"