# Index - Returns the index of a specified item in the list

nums = [2, 6, 5, 2, 0, 4]

nums.index(2)

# Output
0
# 0 index is the position of "2" in the list nums
# This will only return index of the first instance of a value


nums.index(5, 1)
# This wants the index position of the first 5 after the index of 1
# Output
2

nums.index(0, 3, 4)
# This wants the index of 0 between the index of 3 and 4 (inclusive) 
# Output
4


# Count - How many times is an item present in a list

nums.count(2)
# Output
2


