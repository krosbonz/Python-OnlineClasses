# Absolute value - The magnitude of a number regardless of its sign

# abs(6) = 6, abs(-6) = 6
# Works with integers and floats


# Sum - Runs from left to right adding all elements in a list. Can use
# optional starting number

sum([1, 2, 3])
6
# With optional start number
sum([1, 2, 3,], 10)
16

sum([1, 2, 3], -6)
0

# Round - Take any number and it will round it up or down
# optional number of digits to round to

round(1.234)
# Output
1

round(1.344567, 2)
# Output
1.34


# Find the largest absulute value in a list
def max_magnitude(x):
	return max(abs(n) for n in x)



# Sum all even numbers in an unknown list of numbers
def sum_even_values(*args):
    tot = []
    for n in args:
        if n % 2 == 0:
            tot.append(n)
    return sum(tot)

# Better answer
def sum_even_values(*args):
    return sum(x for x in args if x % 2 == 0)


# Sum all floats in an unknown list of arguments
def sum_floats(*args):
    return sum(x for x in args if type(x) == float)