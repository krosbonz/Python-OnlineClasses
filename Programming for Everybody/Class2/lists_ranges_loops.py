#Range

print(range(4))
#Output
[0, 1, 2, 3]

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
#Output
3

print(len(range(friends)))
#Output
[0, 1, 2]


#Loop through list
friends = ['john', 'pete', 'sally']
for i in range(len(friends)):
    buddy = friends[i]
    print('happy new year', buddy)
  
or 

for i in friends:
    print('happy new year', i)
#Both produce the same output