# Function attached to an object (my_list.sort) is a method 
# Funciton on its own just a function

data = [2, 6, 3, 8]

# Append
data.append("black")
print(data)

# Output
[2, 6, 3, 8, 'black']

data.append([1, 0])
print(data)

# Output
[2, 6, 3, 8, [1, 0]]
# If you do a "len(data)" it will return 5 NOT 6. the "[1, 0]"
# is considered a single item



# Extend
data.extend([1, 0])
print(data)

# Output
[2, 6, 3, 8, 1, 0]


# Insert
data.insert(2, 'q')
# This inserts "q" into the 2 index position

# Output
[2, 6, 'q', 3, 8]

# Index position can use negative numbers