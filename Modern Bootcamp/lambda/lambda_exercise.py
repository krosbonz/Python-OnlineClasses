# Write a function called 'interleave' that accepts two strings It should
# return the two stings interwoven or zipped together
interleave('hi', 'by')
# Output
'hbiy'


def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))




# Write a function that accepts a list of numbers. Return list filtering
# out nums not div by 4


def triple_and_filter(x):
    return [t * 3 for t in x if t % 4 == 0]



# Write function that accepts a list of dictionaries and returns concatinated string of 
# the keys

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(x):
    first = list(map(lambda f: f['first'], x))
    last = list(map(lambda l: l['last'], x))
    stuff = [x for x in (zip(first, last))]
    return stuff
    
def extract_full_name(x):
    stuff = [x for x in zip((map(lambda f:f['first'], x)), (map(lambda l:l['last'], x)))]
    for i in stuff:
        print(*i)

def extract_full_name(x):
    stuff = [x for x in zip((map(lambda f:f['first'], x)), (map(lambda l:l['last'], x)))]
    print(stuff)
    

def extract_full_name(x):
    return list(map(lambda f,l: f['first']+" "+ l['last'], x))
    

def extract_full_name(x):
    first = list(map(lambda f: f['first'], x))
    last = list(map(lambda l: l['last'], x))
    return list(map(lambda f,l: f+" "+l, first, last))
    
    
# Final version
def extract_full_name(x):
    return list((map(lambda f:f['first'], x))+ " " +(map(lambda l:l['last'], x)))
    
# Their answer
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
    

