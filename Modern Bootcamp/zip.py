
# Zip - Matches up like indexed items in lists

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

stuff = zip(midterms, finals, students)
list(stuff)
# Output
[(80, 98, 'dan'), (91, 89, 'ang'), (78, 53, 'kate')]

stuff = zip(midterms, finals)
dict(stuff)
# Output
{80: 98, 91: 89, 78: 53}


five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (5, 6)]
list(zip(*five_by_two))
# "*" + list name will "unpack" the list of tuples to form two
# individual tuples
# Output
[(0, 1, 2, 3, 5), (1, 2, 3, 4, 6)]


# Returns dict with {student:highest score} USING LIST COMP
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
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
# Output
{'dan': 89.0, 'ang': 90.0, 'kate': 65.5}




final_grades = dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))



















# # r = dict(zip(students, midterms))
# print(r)

# r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
# print(r)

# r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
# print(r)


# z = zip(
# 	students,
# 	map(
# 		lambda pair: max(pair),
# 		zip(midterms, finals)
# 	)
# )

