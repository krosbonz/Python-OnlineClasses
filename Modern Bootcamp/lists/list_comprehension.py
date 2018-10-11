# List Comprehension - Output a list from manipulating the values
# from and original list

# [_for_in_]

nums = [1, 3, 5]

[x*10 for x in nums]

# Output
[10, 30, 50]

# List Comprehension vs Looping

nums = [1, 2, 3, 4, 5]
double_nums = []

for num in nums:
    double_num = num * 2
    double_nums.append(double_num)
print(double_nums)

# OR

double_nums = [nums * 2 for num in nums]

# Examples of List Comprehension

name = 'colt'

[char.upper() for char in name]
# Output
['C', 'O', 'L', 'T']

friends = ['jim', 'jessee', 'johnny']

[friends[0].upper() for x in friends]
# Output
['Jim', 'Jessee', 'Johnny']

[num*10 for num in range(1,6)]
# Output
[10, 20, 30, 40, 50]

nums = [1, 3, 5, 7]
num_to_string = [str(x) for x in nums]
print(num_to_string)
# Output
['1', '3', '5', '7']