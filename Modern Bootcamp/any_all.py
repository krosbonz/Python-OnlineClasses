# Any or All elements in an interable are truthy 

all([1, 2, 3, 4, 0])
# This would return False because "0" is falsy

any(val for val in [1, 2, 3] if val > 2)
# This would return True because there is at least one element is > 2


# Return True on if all items in list are strings
def is_all_strings(x):
    return all(type(i) == str for i in x)
