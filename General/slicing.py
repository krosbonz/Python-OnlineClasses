# Slicing - Making new lists by taking slices of a current list
# some_list[start:end:interval]
# Very much like range(), but we use ":" and "[]"

some_list = [1, 5, 7, 9]

# Start - Start is inclusive
some_list[1:]
# This goes to the 1 index position inclusive and takes the rest of 
# the list

# Output
[5, 7, 9]


some_list[:]
# or
some_list[:0]
# Same thing and == a copy of the entire original list

# End - End is exclusive
some_list[:2]
# Output
[1, 5]

# Start and End
some_list[1:3]
# Output
[5, 7]

# Negative numbers
# Negative at beginning
some_list[-2:]
# Output
[7, 9]
# Using negative numbers starts at -1 not -0 and slices to the end

some_list[:-1]
# Negative at the end
# Start position is "0" and goes up until one item from the end
# Output
[1, 5, 7]

some_list[1:-1]
# Output
[5, 7]

some_list = [1, 3, 5, 7, 9, 11]

# Step - The number to count at a time
some_list[1::2]
# Output
[3, 7, 11]

some_list[::2]
# Output
[1, 5, 9]

# Step - Negative numbers
some_list[::-1]
# This will reverse a list

some_list[1::-1]
# This says start at index 1 (3), with no end index 
# and reverse direction count by 1
# Output
[3, 1]

some_list[:1:-1]
# Start at 0 index, end at index 1 (exclusive)
# and count backwards by 1
# Output
[11, 9, 7, 5]

some_list[2::-1]
# Start at index 2 (5), there is no end, count backwards by 1
# Output
[5, 3, 1]

color_list = ['red', 'yellow', 'blue']
color_list[1][::-1]
# Selects index 1 (yellow) and slices it
# Output
['wolley']

"hhhhelllloooooooooooo"[::3]
# Output
"hhllloooo"

# Modify lists using slices
some_list[1:3] = ['a', 'b', 'c']
# Output
[1, 'a', 'b', 'c', 7, 9, 11]
