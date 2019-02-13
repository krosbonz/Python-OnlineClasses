# Unpacking Tuples and Lists

# This defined function works fine with a list of numbers...
def sum_all_values(*args):
	print(args)
	total = 0
	for num in args:
		total += num
	print(total)

# sum_all_values(1,30,2,5,6)

# But you couldn't directly feed it a string or a tuple
nums = [1,2,3,4,5,6]
sum_all_values(nums)
# This would cause a traceback

# Instead you pass the variable preceeded by an "*"

sum_all_values(*nums)
# This will "unpack" the items in the list or tuple and then you can 
# loop through them


