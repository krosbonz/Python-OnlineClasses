stuff = range(1,7)

for item in stuff:
    print(item)
    print(item * item)
    print(item * 10)    
    

# range(7) - Gives you 0 thru 6 exclusive of 7
# range(1,8) - Gives you 1 thru 7 exclusive of 8
# range(1,10,2) - Gives you 1 thru 9 exclusive of 10, counting by 2. Can also count
# down by using negative numbers
# range(7,0,-1) - Gives you 7 down to 1


# To print your range, use "list"
stuff = range(10)
list(stuff) 

# Quiz - Add up all odd numbers between 10-20(inclusive)
x = 0

for y in range(10,21):
    if y % 2 != 0:
        x = x + y
print(x)


x = input("how many times should I repeat myself?")

for n in x:
    print("repeat myself" * n)



# Another example of loop and range

x = range(1,21)

for num in x:
    if num % 2 == 0 and num != 4:
        print(f"{num} is even")
    elif num == 13 or num == 4:
        print(f"{num} is unlucky")
    else:
        print(f"{num} is odd")



# Yet another loop example;
x = range(1,10)
for y in x:
    print("\U0001f600" * y)

# This should be shortened to;
for y in range(1,10):
    print("\U0001f600" * y)


# Nested for loop to repeat. This will repeat the 1,10 range three times;
for x in range(3):
    for y in range(1,10):
        print("\U0001f600" * y)
    