# Document functions with """

def documentation():
"""A simple function for balancing the budget"""
    return "hello!"

# You can reference the function documentation
documentation.__doc__
# Output
A simple function for balancing the budget

# This doesn't just work for our own documentation, but for all functions

print.__doc__
# Output
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints 
the values to a stream, or to sys.stdout by default.\nOptional keyword 
arguments:\nfile:  a file-like object (stream); defaults to the current 
sys.stdout.\nsep:   string inserted between values, default a 
space.\nend:   string appended after the last value, default a newline.\nflush: 
whether to forcibly flush the stream."


# When defining functions you must use parameters in a specific order
# 1) parameters 2) *args 3) default params 4) **kwargs

def display_info(a, b, *args, instructor="Colt", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

[1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]