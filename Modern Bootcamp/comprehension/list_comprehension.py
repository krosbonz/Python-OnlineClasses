# List Comprehension - Output a list from manipulating the values
# from and original list

# [_for_in_]

nums = [1, 3, 5]

[x*10 for x in nums]

# Output
[10, 30, 50]

# List Comprehension vs Looping

nums = [1, 2, 3, 4, 5]
double_nums = []

for num in nums:
    double_num = num * 2
    double_nums.append(double_num)
print(double_nums)

# OR

double_nums = [nums * 2 for num in nums]

# Examples of List Comprehension

name = 'colt'

[char.upper() for char in name]
# Output
['C', 'O', 'L', 'T']

friends = ['jim', 'jessee', 'johnny']

[friends[0].upper() for x in friends]
# Output
['Jim', 'Jessee', 'Johnny']

[num*10 for num in range(1,6)]
# Output
[10, 20, 30, 40, 50]

nums = [1, 3, 5, 7]
num_to_string = [str(x) for x in nums]
print(num_to_string)
# Output
['1', '3', '5', '7']


board = [[x for x in range(1, 4)] for y in range(1, 5)]
# The first part - This creates a single list [1, 2, 3]
# The second part - This does everything in the first part for range(1, 5)

# Output
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]  

[["X" if num % 2 != 0 else "O" for num in range(1, 4)] for x in range(1, 4)]
# Working backwards this time...
# We know there will be three lists based on the "for x in rang.."
# The beginning says put an "X" if even or an "O" if odd in range(1, 4)
# or three values in a list

# Output
[['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]



users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# NOTE: You don't need to use u['tweets'] == None or len(u['tweets'] == 0) if 
# we are only looking for True or False. [] is equal to False anyway!

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]