# Interator - An object that can be iterated upon. An object that returns data
# one element at a time when a "next()" is called on it 

# Iterable - An object which will return an iterator when "iter()" is called on it 


# "iter() for the object we want to be iterable"
# "next() for each iteration of the object"
def my_for(iterable):
    iterator = iter(iterable)
    print(next(iterator))


# In this function we would only get the first item in the iterated object;
>>> def my_for(iterable):
...     iterator = iter(iterable)
... print(next(iterator))
...
>>> my_for("thing")
t

# "next()"" needs to be called until all elements of the string, list, etc... 
# have been iterated.

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

# Output
>>> my_for("thing")
t
h
i
n
g

# NOTE: If we didn't use the "try/except" with the "StopIteration" we would see
# a Traceback when the end of the iterated object was reached;
>>> my_for("thing")
t
h
i
n
g
Traceback(most recent call last):
  File "<stdin>", line 1, in < module >
  File "<stdin>", line 4, in my_for
StopIteration


Advanced Iterations

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            it = next(iterator)
            func(it)
        except StopIteration:
            break

# Output
>>> my_for('fast', print)
f
a
s
t

Advanced Iterations II

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            it = next(iterator)
            func(it)
        except StopIteration:
            break

def square(x):
    print(x * x)
    
# Output
>>> my_for([1, 2, 3, 4], square)
1
4
9
16
# In this case the "squre" function was called for "func"
