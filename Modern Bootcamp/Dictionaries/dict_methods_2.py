# Pop, Popitem, Update

stuff = dict(a=1, b=2, c=3)

# Pop - Takes a single argument corresponding to a key in a dict and 
# removes that key/value pair
stuff.pop('a')
# Output
1
# Pop, when run, returns the value to the corresponding key AND
# removes the key/value pair from dict
stuff = {b=2, c=3}

# If the key doesn't exist you will get a Traceback


# Popitem - Removes a random key/value from a dict. It takes no args.
stuff.Popitem()


# Update - Updates key/values in a dictionary with another setof key/value pairs

things = {}
things.update(stuff)

things 
{'a': 1, 'b': 2, 'c': 3}

# If we were to overwrite a value in things...
things ['a'] = 6
{'a': 6, 'b': 2, 'c': 3}

# and then ran update again...
things.update(stuff)

# the value for 'a' would get overwritten back to the orig value
{'a': 1, 'b': 2, 'c': 3}