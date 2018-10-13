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