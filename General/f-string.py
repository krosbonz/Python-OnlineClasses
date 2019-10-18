# Fstrings with string values

fruit = "apple"
ripeness = "unripe"

# Using the older "format" method
sentence = "The {} is {}".format(fruit, ripeness)

# Using the new "fstring" method
sentence = f"the {fruit} is {ripeness}"

print(sentence)

# Output
The apple is unripe


# Fstrings with dictionaries

person = {'name': 'roger', 'age': 10}

sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

# Output
My name is roger and I am 10 years older


# Fstrings with calculations

calculate = f"4 times 10 is equal to {4 * 10}"


# Fstrings with for loops and ranges

for n in range(1, 4):
    sentence = f'The value is {n}'
    print(sentence)

# Output
The value is 1
The value is 2
The value is 3


# Fstring with rounding values

print("How many kilometers do you want to convert to miles?")
kms = float(input())
print(f"OK, you said {kms} kilometers")
miles = kms/1.60934
print(f"{kms} kilometers converts to {round(miles, 2)} miles")