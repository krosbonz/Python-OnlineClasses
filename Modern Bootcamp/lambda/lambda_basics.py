# The idea of the lambda is to have a useful "in-line" command that eliminates
# the need, in this case, for a defined function.

# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

# NOTE: This is just an example. You wouldn't generally use a variable
# with a lambda

# Executing the lambdas
print(square2(7))
print(add(3,10))

# Return the cube of a number
cube = lambda a: a ** 2

print(cube(6))
# Output
36

# An example when you might use a lambda;

import tkinter as tk
# DON'T WORRY ABOUT ANY OF THIS CODE
root = tk.Tk()#=====================
frame = tk.Frame(root)#=============
frame.pack()#=======================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Don't need this function if we use a lambda 
# def say_hi():
#     print("HELLO!")

button = tk.Button(frame, 
                   text="CLICK ME", 
                   fg="red",
                   command=lambda: print("Hello"))



# DON'T WORRY ABOUT ANY OF THIS CODE
button.pack(side=tk.LEFT) #=========
root.mainloop() #===================
# DON'T WORRY ABOUT ANY OF THIS CODE

# Without the lambda you would need the "command=" to call a defined function
# command=say_hi


