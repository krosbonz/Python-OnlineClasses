# For loop
numbers = [1, 3, 6, 2, 5, 6]
for num in numbers:
    print(num * num)

# 1
# 9
# 36
# 4
# etc...

# For loop II
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

for i in sounds:
    result += i
print(result.upper())

# Output
# SUPERCALIFRAGILISTICEXPIALIDOCIOUS



# While loop
stuff = [1, 4, 6, 2, 8, 10]

i = 0
while i < len(stuff):
    print (stuff[i])
    i =+ 1

# The "i < len(stuff)" means while i is less than 6 or the number of 
# items in the list

# While loop using the f statement method
stuff = [1, 4, 6, 2, 8, 10]

i = 0
while i < len(stuff):
    print (f"{i}: {stuff[i]}")
    i =+ 1

# Output
# 0 : 1
# 1 : 4
# 2 : 6 ETC...
