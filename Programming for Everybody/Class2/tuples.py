#Tuples, like strings, are immutable 
#You cannot .sort, .append or .reverse a tuple

#List
x = [1, 3, 5]
x[2] = 7
print(x)
#Output
[1, 3, 7]

#String
y = 'abc'
y[2] = d
print(y)
#Output
Traceback

#Tuple
z = (5, 4, 3)
z[2] = 6
print(z)
#Output
Traceback 

#Tuples can be put on both sides of an equation
(x,y) = (9, 'fred')
print(y)
#Output
fred

#Tuples are comparble
(0, 23, 45) < (1, 55, 99)
(0, 1, 2000000) < (0, 3, 4)
('jones', 'sally') < ('jones', 'sam')
('jones', 'sally') < ('adam', 'sam')
#Output for all
True
#Only the first item is looked at unless they are the same, then it goes to the next item

#Sorting Tuples (by key)
#.sort doesn't work, but the function "sorted" does
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
#Output of "t" is;
[('a', 10), ('b', 1), ('c', 22)]
#This creates a list of tuples
#From there you do a for loop to sort by key;
for k,v in sorted(d.items()):
    print(k,v)
#Output
a 10
b 1
c 22

#Sorting Tuples (by value)
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
#This says, for each value in dict "c", add to the list "tmp"
#Notice we have reversed the key/value pair to be value/key in the list "tmp"
print(tmp)
#Output
[(10, 'a'), (1, 'b'), (22, 'c')] #Value/key pairs

tmp = sorted(tmp, reversed=True) #Sort high to low
print(tmp)
#Output
[(22, 'c'), (10, 'a'), (1, 'b')]

#Ten most common words in a file using val/key pair
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
#For each key/value pair in dict "counts", create variable "newtup" which creats val/key tuples
#Then append that to the list "lst"

#Now sort the list highest to lowest
lst = sorted(lst, reversed=True)

for val,key in lst[:10]:
    print(key, val)
#For each val/key pair in list "lst", give me the first 10


#BONUS - A faster way to sort once you have the dictionary. In this case "counts"
print(sorted ([(v,k) for k,v in counts.items()]))
