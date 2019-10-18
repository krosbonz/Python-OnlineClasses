# Unpacking - Dictionary

# Same concept as unpacking Tuples and Lists
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(names) 
# This will not work to pass the dictionary to the def funtion

display_names(**names)  
# It requires the use of double asterisks "**"

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")
# **kwargs is comprised of only those items that are NOT a,b,c

add_and_multiply_numbers(**data) 

# Output
7
OTHER STUFF....
{'d': 55, 'name': 'Tony'}

# You can also add to the dictionary "data"
add_and_multiply_numbers(**data, cat='blue')

# Output
7
OTHER STUFF....
{'d': 55, 'name': 'Tony', 'cat': 'blue'}

