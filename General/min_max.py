names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

[len(name) for name in names)]
# Output
[4, 6, 4, 3, 10]

# finds the minimum length of a name in names
min(len(name) for name in names) 
# Output
3

# Find the max length of a name in names
max(len(n) for n in names)
# Output
10

# find the longest name itself
max(names, key=lambda n:len(n)) 
# Output
Ollivander


songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) 
# Output
{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] 
# Output
YMCA


# Return the min and max of a list in a tuple
def extremes(x):
	return (min(x),max(x))


# Find the largest absulute value in a list
def max_magnitude(x):
	return max(abs(n) for n in x)