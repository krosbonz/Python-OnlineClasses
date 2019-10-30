# Yield

"""The yield statement suspends function’s execution and sends a value 
back to caller, but retains enough state to enable function to resume where 
it is left off. When resumed, the function continues execution immediately 
after the last yield run. This allows its code to produce a series of values 
over time, rather them computing them at once and sending them back like a list."""

# A "generator" is any function that contains "yield". 
# Yield generators only return one element of the iterated object each time through

def nextSquare():
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True:
        yield i*i                 
        i += 1  # Next execution resumes from this point      
  
# Driver code to test above generator function 
for num in nextSquare():
    if num > 100:
         break    
    print(num)

# Another example for "yield"

def week(days):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day

days_week = week()
# And then create a variable for the defined function

# Then call the built in "next()" function, we will see one element in the
# iteration through the days each time through 
>>> next(day_week)
'Monday'
>>> next(day_week)
'Tuesday'
>>> next(day_week)
'Wednesday'

# Infinite Generator

def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1
        

# Output
>> > stuff = current_beat()
>> > next(stuff)
1
>> > next(stuff)
2
>> > next(stuff)
3
>> > next(stuff)
4
>> > next(stuff)
1

def make_song(max, bev="kombucha"):
    count = 0
    while x in range(max + 1) > count:
        yield count
        count += 1
    #print("'Only 1 bottle of kombucha left!'")
    #f"{max} bottles of {bev} on the wall"
