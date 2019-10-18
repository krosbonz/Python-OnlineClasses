# Set comprehension

{x**2 for x in range(10)}

# Output
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# There is no order

# Difference between a set and a dictionary
{x:x**2 for x in range(10)}

# Output
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

{char.upper() for char in 'hello'}

# Output
{'H', 'L', 'O', 'E'}
# Because it is as set, no duplicate values are returned


string = 'hello'
{char for char in string if char in 'aeiou'}

# Output
{'e', 'o'}

len({char for char in string if char in 'aeiou'})

# Output
2

len({char for char in string if char in 'aeiou'}) == 5
# Output
False