# Scope - Variables created in a function are "scoped" to that function

# Global vs Local

# In this example "name" is a global variable because it is outside the function
name = 'mickey'

def say_hello():
    return f"say hello to {name}"
# In this instance the global "name" variable can be used in the function
# but it cannot be manipulated in any way

# To manipulate a variable it must reside in the function
def say_hello():
    name = 'mickey'
    return f"say hello to {name}"

# Or the varialble must be declared global within the function

total = 0

def increment():
    global total
    total += 1
    return total

# Non-Local
# Variable "count" is not global, but it isn't local to inner() either. 
# In order to use "count" it must be declared "nonlocal" in the nested function 

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

