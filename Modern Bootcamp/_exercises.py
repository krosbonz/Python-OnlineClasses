# Define function, accepts multiple lists, returns True if contains 
# Python keyword


from keyword import iskeyword

def contains_keyword(*args):
    return any([x for x in args if iskeyword(x)])
    
        


