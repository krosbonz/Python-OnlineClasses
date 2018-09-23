

first_list = [1, 4, 6, 8]

# Clear - Remove all items from a list
first_list.clear()
print(first_list)

# Output
[]


# Pop - Remove an item given the position in the list. 
first_list.pop(1)
print(first_list)

# Output
[4, 6, 8]

# NOTE: Without declaring a position the last item in a list will be removed

# Create a variable using pop and the index of a list
new_list = first_list.pop()
print(new_list)
print(first_list)

# Output
8
[1, 4, 6]

# Remove - Remove the first item from the list whose value is x

new_list.remove(4)

# Output
[1, 6, 8]