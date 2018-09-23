# Reverse - Simply reverses the items in a list

nums = [2, 6, 5, 2, 0, 4]

nums.reverse()
print(nums)
# Output
[4, 0, 2, 5, 6, 2] 


# Sort - Sort low to high or alphabetically
nums.sort()
print(nums)

# Output
[0, 2, 2, 4, 5, 6]


# Join - Combining lists of strings

words = ['the', 'car', 'moves']
' '.join(words)
# whatever preceeds ".join" will be placed between the string values 
# during contatination

# Output
'the car moves'

name = ['mr', 'jones']
'. '.join(name)

# Output
'mr. jones'

# Join used in a variable
names = ['jim', 'john', 'harry', 'frank']
friends = ", ".join(names)

# Output
friends
'jim, john, harry, frank'
names
['jim', 'john', 'harry', 'frank']