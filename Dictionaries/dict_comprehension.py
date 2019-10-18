# Syntax for dictionary comprehension is 
# {_ : _ for _ in _}

# This will iterate over keys by default, but will iterater over
# key and values using .items()
nums = dict[first=1, second=2, third=3]

squard = {key:value ** 2 for key,value in nums.items()}
# The key (first, second, third) remains as is, but value gets squared

# Output
{'first': 1, 'second': 4, 'third': 9}


# Manipulating both key and value
person = dict['name'= 'mike', 'city'= 'new york', 'pet'= 'yes']

person_proper = {key.upper(): value.upper() for key,value in person_proper.items()}

# Output
{'NAME': 'MIKE', 'CITY': 'NEW YORK', 'PET': 'YES'}

# Manipulate key only
person_upper = {(key.upper() if key is 'pet' else key):value.upper() for etc...}


# Making a dictionary
{num: num ** 2 for num in [1, 2, 3, 4, 5]}

# Output
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Align two strings
str1 = "ABC"
str2 = "123"

{str1[i]: str2[i] for i in range(0, len(str1))}

# Output
{'A': '1', 'B': '2', 'C': '3'}


# Conditional Comprehension
nums  = [1, 2, 3, 4]

{num: ("even" if num in num % 2 == 0 else "odd") for num in nums}

# Output
{1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
