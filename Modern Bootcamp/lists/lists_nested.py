# Nested Lists

nest_list = [[1, 2, 3][4, 5, 6][7, 8, 9]]

# To access an item within a nested list
nest_list[0][1]

nest_list[0][2]
# Output
3

nest_list[-1]
# Output
[7, 8, 9]

nest_list[0][-1]
# Output
3

nest_list[-1][1]
# Output
8

# Printing values in nested lists

for l in nest_list:
    for x in l:
        print(x)
# The first variable (l) in the first for loop is for each nested list
# The nested for loop is for each item within each nested list

# Output
1
2
3
4
5
6
7
8
9
