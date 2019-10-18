# Dictionaries - A data structure with key value pairs.

stuff = {
"name": "michael",
"color": "black",
"car": "bmw",
"pet": False
}

# Dict function = Assign values to keys by passing in keys and values
# separated by an "=".

stuff2 = dict(name='roger', age=27.5)
print(stuff2)

# Output
{'name': 'roger', 'age': 27.5}


# To get values from a dictionary

stuff['name']
# Output
michael

# Variables for keys in a dictionary

>>> something = 'name'
>>> something
'name'
>>> stuff[something]
'michael'


# Accessing all values/keys/items in a dictionaries

for x in stuff.values():
    print(x)
# Produces a list of values from the dict

stuff.values()
# Produces a list of dictionary values
dict_values(['michael', 'black', 'bmw', False])

# Or

for x in stuff.keys():
    print(x)

stuff.keys()
# Same as above

for x,y in stuff.items():
    print(x,y)
# To loop through "items" you must provide values for both key and value
# Output
name michael
color black
car bmw
pet False

# Loop using Fstring
for x,y in stuff.items():
    print(f"Key is {x}, and value is {y}")

stuff.items()
# Produces a list of tuples containing key/value pairs
dict_items([('name', 'michael'), ('color', 'black'), ('car', 'bmw'), ('pet', False)])


# Test for the existence of a key
"name" in stuff

# Output 
True

# Test for existence of a value
"michael" in stuff.values()

# Output
True