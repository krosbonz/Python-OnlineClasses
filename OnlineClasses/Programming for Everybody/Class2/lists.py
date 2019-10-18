#Changing an item within a list
lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto)

#Output would now be;
[2, 14, 28, 41, 63]


#"lotto" is mutable (changeable) because we can change an index within "lotto"
lotto = [2, 14, 26, 41, 63]
lotto[0]

list('lotto')
#Output
['l', 'o', 't', 't', 'o']

list(lotto)
#Output
[2, 14, 26, 41, 63]

#While the brackets remain open, a list can be put on multiple lines
lotto = ['stuff',
         'things',
         'garbage',
         'trash',]
list(lotto)
#Output
['stuff', 'things', 'garbage', 'trash']


#"frt" is immutable because it cannot be indexed
frt = 'banana'
frt[0]
#This cannot be done. It will produce a traceback


#len() works with lists to produce the number of elements in a list
lotto = [2, 14, 26, 41, 63]
print(len(lotto))