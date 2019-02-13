# *args - Allows you to pass in any number of arguments without calling
# each one independantly

def sum_up(num1,num2, num3):
    return num1+num2+num3

def sum_up(*args)
    total = 0
    for x in args:
        total += x
    return total
# NOTE: The parameter does not need to be "args" it is just common

# You can also have other parameters along with *args
def sum_up(num1,*args)
    print(num1)
    total = 0
    for x in args:
        total += x
    return total

print(sum_up(4,6,7, 5, 9))
# Output
4
27
# 4 will be printed and the remainder will be summed

def include_info(*args):
    if 'stuff' in args and 'car' in args:
        return "it's all here"
    return "not all here"
# NOTE: You don't need "else:" because once a def hits a return
# the function is done

print(include_info(1, 'a', 'stuff', 3, 'car'))
# Output
"it's all here"


# **kwargs - Output will be a dictionary

def fav_color(**kwargs):
    print(kwargs)

fav_color(mickey='black', steely = 'purple', silly = 'silver')

# Output
{mickey:'black', steely:'purple', silly:'silver'}

# Looping through **kwargs
def fav_color(**kwargs):
    for person, color in kwargs.items:
        print(f"{person}'s favorite color is {color}")

     
def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not sure who this is..."
# Output
# print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

# NOTE: The options above pass in a single key/value pair, but you 
# could pass multiple without issue



# **kwargs Exercise
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix']+word
    elif 'suffix' in kwargs:
        return word+kwargs['suffix']
    return word

# The last line above doesn't require "else:"