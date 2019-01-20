from random import random

def flip_coin():
    # random() returns a random number between 0 and 1
	if random() > 0.5:
		return "HEADS"
	else:
		return "TAILS"

print(flip_coin())
# Output
HEADS
or
TAILS



def generate_evens():
    evens = []
    [evens.append(x) for x in range(1,50) if x % 2 == 0]
    return evens

print(generate_evens())
# Output
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 
30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

# Above can be cleaner and shorter
def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]