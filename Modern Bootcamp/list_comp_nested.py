
board = [[x for x in range(1, 4)] for y in range(1, 5)]
# The first part - This creates a single list [1, 2, 3]
# The second part - This does everything in the first part for range(1, 5)

# Output
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]  

[["X" if num % 2 != 0 else "O" for num in range(1, 4)] for x in range(1, 4)]
# Working backwards this time...
# We know there will be three lists based on the "for x in rang.."
# The beginning says put an "X" if even or an "O" if odd in range(1, 4)
# or three values in a list

# Output
[['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]