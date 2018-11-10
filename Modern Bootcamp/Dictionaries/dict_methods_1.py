# Clear, Copy, Get

things = dict(a=1, b=2, c=3)

# Clear - Clear the contents of a dictionary
things.clear()

# Output
things{}

# Copy - Copy a dictionary
stuff = things.copy()

stuff == things 
True

stuff is things
False

# Get - Retrieves values from dictionaries. Won't error if key isn't there.
stuff = dict(a=1, b=2, c=3, d=4)

stuff['a']
# Output
1

stuff['e']
# Output
# Traceback

stuff.get['e']
# Output
'None'