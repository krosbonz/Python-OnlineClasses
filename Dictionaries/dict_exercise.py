person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

str1 = []
str2 = []
# use the person variable in your answer
for i in person:
    str1.append(i[0])
    str2.append(i[1])
answer = {str1[i]: str2[i] for i in range(0, len(str1))}
print(answer)


# Now the way it should have been done...

# Using a dictionary comprehension 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

# An alternate solution using a dict comprehension, without 
# any references to list indexes:
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

# Finally, a really simple solution.  If you have a list of pairs, 
# you can very easily turn it into a dictionary using dict() 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)