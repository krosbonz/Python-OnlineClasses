# Map - Standard function that accepts at least two arguments, a function and an iterable
# (can be iterated over) like lists, tuples, dictionaries, strings, sets

# Runs the lamda for each value in the iterable and returns a map object
# which can be converted to a data object

nums = [2, 4, 6, 8]

doubles = map(lambda x: x * 2, nums)
# Running doubles would create a map object
doubles
# Output
<map object at 0x000001B67164EBA8>
# You can then iterate over doubles
for x in doubles:
    print(x)
# Output
4
8
12
16

# The above using a function;
nums = [2, 4, 6, 8]

def double(x): return x * 2

doubles = (map(double, nums))
list(doubles)


# Or you can add the list function to convert it inline
doubles = list(map(lambda x: x * 2, nums))

# Another example;
people = ['Darcy', 'Chris', 'Dan', 'Steve']

peeps = list(map(lambda x: x.upper(), people))

# Another example;
names = [{'first': 'Rusty', 'last': 'Jones'}, {'first': 'Harry', 'last': 'Henderson'}, 
{'first': 'Steve', 'last': 'Austin'} ]

first_names = list(map(lambda x: x['first'], names))


# Function that returns a list with each item in list decremented by 1
def decrement_list(x):
    return list(map(lambda n: n -1, x))
# Run
decrement_list([1, 2, 3])
# Output
[0, 1, 2]



# Using Map and Filter
# This creates a list of usernames filtered on users with no tweets
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))


# Using Map and Filter 2
names = ['Lassie', 'Colt', 'Betsy']

list(map(lambda name: f"Hello {name}", filter(lambda char: len(char) < 5, names)))
# Output
['Hello Colt']


