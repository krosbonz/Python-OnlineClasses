# Default values are used when all arguments are not passed into the function

# Standard function that requires two arguments
def math(a,b):
    return a + b

# This says if no second argument is passed use "2" by default
def math(a, b=2):
    return a + b


# A more complex example using "fn" which means function

def add(a,b):
    return a + b

# In this example if no mathematical equation is provided, default to "add"
def math(a,b, fn=add):
    return fn(a,b)

def subtract(a,b):
    return a - b

# This uses the default and goes to the "add" function
math(2,2)
# Output
4

# This goes to the "subtract" function 
math(2, 2, subtract) 


# Keyword Arguments
# NOTE: Order doesn't matter
def exponent(num, power=2):
    return num ** power

print(exponent(power=6, num=2))



# Exercise - for certain animal arguments, return animal sound or "?", default dog
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

# Or using dictionary
noises = {
    "dog": "woof", 
    "pig": "oink", 
    "duck": "quack", 
    "cat": "meow"
}
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# Or using dictionary, more compact
def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')