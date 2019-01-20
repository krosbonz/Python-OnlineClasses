# Tuples, unlike lists are immutable, meaning they cannot be changed

# Commonly used to represent an unchanging list, such as the days of the week
# or months of the year.

# Tupples can be used as the key in a dictionary but lists cannot
location = {(36.3456, 39.3452): 'Tokyo', (45.5675, 23.2345): 'Berlin'}

# Some dictionary methods like ".items()" return tuples
cat = {'name': 'harry', 'type': 'tabby'}
cat.items()
# Output
dict_items([('name', 'harry'), ('type', 'tabby')])


# Methods for tuple; count and index

# Count - shows how many of an item is in a tuple
x = (1, 1, 3, 4, 4, 4, 7)
x.count(1) 
# Output
2

# Index - returns the index of a given value in a tuple
x.index(1)
# Output
0
# Note: Only the first matching value will be identified

