# Filter - Like map takes two parameters, one iterable. 
# Will filter out based on expression or condition

l = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 = 0, l))

evens
# Output
[2, 4, 6]


names = ['Angela', 'Jon', 'Adam', 'Pete']
a_names = list(filter(lambda n: n[0]=='A', names))

# Run
a_names
# Output
['Angela', 'Adam']


users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#extract inactive users (no "tweets")using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

# NOTE: You don't need to use u['tweets'] == None or len(u['tweets'] == 0) if 
# we are only looking for True or False. [] is equal to False anyway!

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))


