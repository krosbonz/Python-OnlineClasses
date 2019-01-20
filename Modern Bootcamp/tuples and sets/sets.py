# Sets - Collection of data with no duplicate values, elements are ordered
# you cannnot index, no key values

# You pass the "set" function like the "dict" function to create a set

s = set{1, 3, 4, 5, 5, 5}

# s would equal
s = {1, 2, 3, 4, 5}
# Only unique values would be returned, and they would be in order

cities = {'boston', 'detroit', 'paris', 'berlin', 'boston', 'las angeles'}
print(set(cities))
# Output
{'berlin','boston', 'detroit', 'las angeles', 'paris'}

# Convert to list with only unique values
print(list(set(cities)))

# Number of unique values
print(len(set(cities)))
# Output
6

# Functions to use with "set"
# Add, Remove, Discard, Copy, Clear, Set Math
s = {1, 2, 3, 4, 5}
s.add(7)

s.remove(2)

s.discard(8)
# Discard allows you to remove a value without getting an error
# if the value doesn't exist

another_2.copy()
# Copies a set

s.clear()
# Clears a set

# Set Math
set1 = {'bob', 'jon', 'harry', 'tom'}
set2 = {'jon', 'phil', 'tom', 'pete'}

# Join multiple sets
set1 | set2
# Output
{'bob', 'jon', 'pete', 'phil', 'harry', 'tom'}

# Found in both sets
set1 & set2
# Output
{'jon', 'tom'}



