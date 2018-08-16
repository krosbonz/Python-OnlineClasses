# Create a loop to repeat

x = input("how many times should I repeat myself? ")
x = int(x)
print("repeat myself \n" * x)

# Or

times = input("how many times should I repeat myself? ")
times = int(times)

for time in range(times):
    print("repeat myself")