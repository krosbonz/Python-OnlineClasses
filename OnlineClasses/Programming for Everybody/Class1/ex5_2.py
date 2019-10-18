largest = -1
smallest = None
list = []
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num_ = int(num)
    except:
        print("Invalid input")
        continue
    #print(num)
    list.append(num_)

for small in list:
    if smallest is None:
        smallest = small
    elif small < smallest:
        smallest = value

for large in list:
    if large > largest:
        largest = large

print("Maximum is", largest)
print("Minimum is", smallest)
