# While loop with break
while True:
    command = input("Type 'exit' to exit: ")
    if command == 'exit':
        break




# For loop with break
for x in range(0,100):
    print(x)
    if x == 3:
        break


# For loop with break II
times = int(input("how mnay times have I told you: "))
for time in range(times):
    print("clean up after yourself")
    if time >= 4:
        print("tired of talking to myself")
        break

# Generate random number until 5
from random import randint
i = 0
while True:
    number = randint(1,10)
    i += 1
    if number == 5:
        break
