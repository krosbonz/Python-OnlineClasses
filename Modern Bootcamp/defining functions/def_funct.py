# Functions - Process for executing a task. More simply, code that can be reused.
# Helps code stay "dry" > don't repeat yourself

# Structure
def name_of_function():

def say_hi():
    print('hi!')

# To invoke this def 
say_hi()
# Output
hi!

# Return values from functions
def square_of_seven():
    return 7**2

result = square_of_seven()
print(result)
# Output
49

# NOTE: "return" exits a function, so even if there was more code directly
# after "return 7**2" it would not run

def square_of_seven():
    return 7**2
    print('yo mama')
# 'yo mama' would never print!

# This would work
def square_of_seven():
    print('yo mama')
    return 7**2
    