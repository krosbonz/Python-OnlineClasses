tasks = ["Install Python", "Bake Cake", "Eat Lobster"]

print(tasks[1])
# Bake Cake

len(tasks)
# 3

# Printing lists
stuff = range(1,10)
stuff
# range(1,10)
list(stuff)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# or... quicker
stuff = list(range(0,10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Indexing a list
stuff[2]
# 3
stuff[-2]
# 7

# Check if a value is in a list
10 in stuff
# False
3 in stuff
# True

# Change list items
stuff[2] = 7