
# Zip - Matches up like indexed items in lists

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# Lists
stuff = zip(midterms, finals, students)
list(stuff)
# Output
[(80, 98, 'dan'), (91, 89, 'ang'), (78, 53, 'kate')]


# Dictionary
stuff = zip(midterms, finals)
dict(stuff)
# Output
{80: 98, 91: 89, 78: 53}

# Get max for each pair
final_grade = [max(pair) for pair in zip(midterms, finals) ]
print(final_grade)
# Output
[98, 91, 78]

# Get max and add list with dict comprehension
final_grade = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# t[0] = students, t[1] = midterms and t[2] = finals
# So, this makes eash student's name the key 
# Then takes the max of the two remaining lists
# and makes a dictionary
# Output
{'dan': 98, 'ang': 91, 'kate': 78}


# Returns dict with {student:highest score} USING MAP+LAMBDA
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)
# Output
{'dan': 98, 'ang': 91, 'kate': 78}


# returns dict with student:average score
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)
# This zips "students" with the average grade of the zip of "midterm" and "finals"
# Output
{'dan': 89.0, 'ang': 90.0, 'kate': 65.5}

final_grades = dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))


# Unpacking a zip list
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (5, 6)]
list(zip(*five_by_two))
# "*" + list name will "unpack" the list of tuples to form two
# individual tuples
# Output
[(0, 1, 2, 3, 5), (1, 2, 3, 4, 6)]

