# Yield

"""The yield statement suspends function’s execution and sends a value 
back to caller, but retains enough state to enable function to resume where 
it is left off. When resumed, the function continues execution immediately 
after the last yield run. This allows its code to produce a series of values 
over time, rather them computing them at once and sending them back like a list."""

# A "generator" is any function that contains "yield". Also, generators can only be
# run once. 

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