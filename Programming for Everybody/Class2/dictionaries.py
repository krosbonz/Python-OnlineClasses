#Dictionaries - key / value pairs
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
#Output
print(purse)
{'money': 12, 'candy': 3, 'tissues': 75}

print(purse['candy'])
#Output
3

#Manipulating Values
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
#Output
print(purse)
{'money': 12, 'candy': 5, 'tissues': 75}

#Dictionary For loops
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
#Output
{'csev': 2, 'cwen': 2, 'zqian': 1}

#Simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
#This is saying get the current count for "name" or zero(if not seen before) and add 1
print(counts)
#Output
{'csev': 2, 'cwen': 2, 'zqian': 1}
