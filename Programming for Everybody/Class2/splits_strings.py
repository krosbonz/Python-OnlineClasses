#Splits by default uses spaces as the delimiter
abc = 'this was dumb'
stuff = abc.split()
print(stuff)
#Output
['this', 'was', 'dumb']

print(len(stuff))
#Output
3

print(stuff[0])
#Output
this

for i in stuff:
    print(i)
#Output
this
was
dumb

#Splits can use any defined delimiter
abc = 'first;second;third'
stuff = abc.split(';')
print(stuff)
#Output
['first', 'second', 'third']


#Split and index
addy = 'from michael.hauck@lawrencegeneral.org sat jan 5 09:14:16 2017'
piece1 = addy.split()
print(piece1[1])
#Output
michael.hauck@lawrencegeneral.org

#Double split and index
addy = 'from michael.hauck@lawrencegeneral.org sat jan 5 09:14:16 2017'
words = addy.split()
smpiece = words[1]
print(smpiece)
smallerpiece = smpiece.split('@')
print(smallerpiece)
print(smallerpiece[1])
#Output
['michael.hauck', 'lawrencegeneral.org']
lawrencegeneral.org

