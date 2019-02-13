# Enter a number 1-7 and return a day of the week or "None" if >7 or <1
def return_day(x):
    days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday",
    6:"Friday", 7:"Saturday"}
    return days.get(x, None)

# Better option
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
         
# Return last element in a list
def last_element(a):
    if a == []:
        return None
    else:
        return a[-1]

# Better option - If list (l) exists, meaning if it contains data
# return last element
def last_element(l):
    if l:
        return l[-1]
    return None


# Two parameters, if first > return "first greater" else "second greater"
def number_compare(a,b):
    if a > b: return "First is greater"
    elif a == b: return "Numbers are equal"
    return "Second is greater"


# Two parameters, first = word, second = letter return num times letter in word
# case insensitive
def single_letter_count('word','letter'):
    return word.lower().count(letter.lower())


# One parameter, return dictionary key/value = letter/count of letter
def multiple_letter_count(word):
    return {x: word.count(x) for x in word} 



# Four params, (list, command, location, value)
def list_manipulation(lst,com,loc,val=None):
    if com == 'remove':
        if loc == 'end':
            return lst.pop()
        elif loc == 'beginning':
            return lst.pop(0)
    else:
        if loc == 'end':
            lst.append(val)
            return lst
        elif loc == 'beginning':
            lst.insert(0,val)
            return lst

# Better option
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection


# Determine if palindrome, return True or False
def is_palindrome(string):
    lst = []
    
    for x in string:
        lst.append(x)
    lst_rev = lst[::-1]
    if lst == lst_rev:
        return True
    else:
        return False

# Better option
def is_palindrome(string):
    return string == string[::-1]


# frequency of item in list
def frequency(lst,cnt):
    return lst.count(cnt)



# Product of all even numbers in a list
def multiply_even_numbers(lst):
    prd = 1
    for x in lst:
        if x % 2 == 0:
            prd *= x
    return prd
    

# Capitalize first letter of string
def capitalize(str):
    return str.capitalize()

# Accepts a list and returns only truthy values
# I had this;
def compact(lst):
    for x in lst:
        if bool(x) != True:
            lst.remove(x)
    return lst

# This is why it kept failing;
# "Falsy values will evaluate to false, but they don't have to be literally 
# equal to the False boolean. See the documentation on Truth Value Testing, 
# Example; empty lists are considered false, but this doesn't 
# mean they are equivalent to False"

# What I used after looking at Stackoverflow;
def compact(lst):
    lst2 = [x for x in lst if x]
    return lst2

# Better option
def compact(l):
    return [val for val in l if val]
    
# Function accepts two lists, returns overlap between them
def intersection(lst1, lst2):
    combo = []
    for x in lst1:
        if x in lst2:
            combo.append(x)
    return combo

# Better solution - List comprehension
    combo = [x for x in lst1 and x in lst2]
    return combo

# Or - Sets solution
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

# For each item in a list run through funct "isEven" and determine
# True or False

def isEven(num):
    return num % 2 == 0

def partition(lst, isEven):
    truthy = []
    falsy = []
    for x in lst:
        if isEven(x) == True:
            truthy.append(x)
        else:
            falsy.append(x)
    return [truthy,falsy]
# NOTE: I keep forgetting I don't need "==True" because that is understood

# Another solution
def partition(lst, isEven):
    return [[val for val in lst if isEven(val)], [val for val in lst if not isEven(val)]]