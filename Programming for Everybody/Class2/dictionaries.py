#Dictionaries - key / value pairs
purse = dict()
#Add to dictionary
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

#get() part I - Simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
#The first part - counts[name] says add variable "name" to dictionary  "counts"
#The second part - "name" is the key and "0" is the default value for the key if none exits. (video 9.2)
#This is saying get the current count for "name" or zero if "name" not previously counted, and add 1
#Used to count how often a key is present in a dictionary
print(counts)
#Output
{'csev': 2, 'cwen': 2, 'zqian': 1}

#get() part II
#get() returns a value for a given key. If no value exits it returns None.
stuff = dict()
print(getattr.stuff('candy', -1))
#Output
-1
stuff = {'Name': 'Amy', 'Age': 7,}
print(stuff.get('Name', 'Amy'))
print(stuff.get('Age'))
print(stuff.get('School'))
#Output
Name Amy
Age 7
School None


#Dictionary with input, splitting and counting
smallfile = input('Enter a file name: ')
stuff = open(smallfile)

counts = dict()
for line in stuff:
#Split the line of text into individual words
    words = line.split()
        for word in words:
#Updates the count of each word. Works for new words or updates the count for existing words
            counts[word] = counts.get(word,0) + 1
print('Counts', counts)


#From the count above find the most repeated word and how many times it was repeated
bigword = None
bigcount = None
for word,count in words.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


#Dictionary with for loop
counts = {'chuck' : 5, 'steve' : 34, 'bryan' : 12}
for i in counts:
    print(i)
#Output
chuck
steve
bryan

counts = {'chuck' : 5, 'steve' : 34, 'bryan' : 12}
for i in counts:
    print(i, counts[i])
#Output
chuck 5
steve 34
bryan 12


#Retrieving keys, values and the combination(items)
counts = {'chuck' : 5, 'steve' : 34, 'bryan' : 12}
print(list(counts))
#Output
['chuck', 'steve', 'bryan']

print(counts.keys())
#Output is the same
['chuck', 'steve', 'bryan']

print(counts.values())
#Output
[5, 34, 12]

print(counts.items())
#Output both key and value tuplit
[('chuck', 5), ('steve', 34), ('bryan', 12)]


#Using two interation values
counts = {'chuck' : 5, 'steve' : 34, 'bryan' : 12}
for k,v in counts.items():
    print(k, v)
#Output
chuck 5
steve 34
bryan 12

#And get largest value
largest = -1
theword = None
for k,v in counts.items():
    if v > largest:
        largest = v
        theword = k

