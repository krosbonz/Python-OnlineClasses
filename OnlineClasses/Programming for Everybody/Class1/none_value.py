smallest = None
print("Before")
for value in [9, 12, 3, 41, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)
