# Passing a single parameter to a function
# Example 1
def square(num):
    return num * num

print(square(4))
print(square(8))
# Output
16
64

# Example 2
def happy_bday(name):
    print(f"Happy bday {name}")

happy_bday("johnny")
# Output
happy bday johnny

# NOTE: The passed parameter doesn't exist outside the function, so "name"
# cannot be used later like "print(name)" because that parameter won't be 
# known to python


# Passing multiple parameters to a function
# Example 1
def add_up(a,b):
    return a + b

add_up(2,3)
# Output
5

# NOTE: Parameters are what is inside the function definition,
# but when they are passed when running the code they are called arguments
# i.e. in the above example, "a" and "b" are parameters, "2" and "3" are arguments

# Using f-string
def yell(cap):
    return (f"{str.upper(cap)}!")

yell('jon')
# Output
'JON!'

# Or by using format() method
def yell(cap):
    return "{}!".format(cap.upper())





