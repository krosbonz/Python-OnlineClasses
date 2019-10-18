# Fromkeys - Pass two arguments, assigns the second as a value to the first

letter = {}.fromkeys('a', 'b')
# "{}"" is the same as using "dict"
letter = dict.fromkeys('a', 'b')

# Output
{'a':'b'}

# Used most often to assign the same value to many keys
bio = {}.fromkeys(['name', 'address', 'email'],'unknown')

bio
# Output
{'name': 'unknown', 'address': 'unknown', 'email': 'unknown'}

# It's important to know the first value will be interated 
# and the value will be applied to each item in the intial argument

test = {}.fromkeys('one', 'unknown')

# Output
{'o':'unknown', 'n':'unknown', 'e':'unknown'}

# Instead, enter first argument as a list
test = {}.fromkeys(['one'], 'unknown')

# Output
{'one':'unknown'}


# You can also use ranges
stuff = {}.fromkeys(range(1,4),'unknown')

# Output
{1: 'unknown', 2: 'unknown', 3: 'unknown'}

