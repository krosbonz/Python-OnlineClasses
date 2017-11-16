#Contatenation
a = [1, 2, 3]
b = [4, 5, 6]
y = a + b
print(y)
#Output
[1, 2, 3, 4, 5, 6]

#Slicing
t = [23, 45, 4, 2, 25]
t[:3]
#Output
[23, 45, 4]
etc...

#Build list from scratch
stuff = list()

#Append list
stuff = list()
stuff.append(9)
stuff.append('banana')
print(stuff)

#Is something in list?
some = [1, 5, 9, 45, 6]
5 in some
#Output
True

20 not in some
#Output
True

#List functions
nums = [10, 4, 34, 3, 10, 24]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#Input, while loop, average of input
stuff = list()
while True:
    num = input('Enter a number: ')
    if num == 'done' : break
    value = float(num)
    stuff.append(value)
    
print('Average: ', sum(stuff)/len(stuff))