# Sorted - Used to sort dictionaries and tuples

nums = [1, 6, 9, 3, 5, 4]

sorted(nums)
# Output
[1, 3, 4, 5, 6, 9]

# The difference between sort and sorted is that sort will sort a list in place
# sorted makes a copy of the list, tuple, dict and returns that item sorted

# Sorted - Reverse
sorted(nums, reverse = True)
# Output
[9, 6, 5, 4, 3, 1]


# Sorting more complex dictionaries
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# The most basic method is to use "len"
sorted(users, key=len)
# This will simply sort based on the most keys (in key/value pairs) in dict

# To sort users by their username
sorted(users,key=lambda user: user['username'])
# In this case "user:" is simply a parameter. It could be called anything.


# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)


# Another example
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])



# Reversed - A way to reverse any interator
nums = [1, 2, 3, 4, 5,6]

reversed(nums)
