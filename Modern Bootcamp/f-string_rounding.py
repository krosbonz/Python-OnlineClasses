# The f-string allows mixing of floats, integers, etc... with
# strings. Notice the "f" and the curly brackets. This makes up the f-string. 

print("How many kilometers do you want to convert to miles?")
kms = float(input())
print(f"OK, you said {kms} kilometers")
miles = kms/1.60934
print(f"{kms} kilometers converts to {round(miles, 2)} miles")

# As you can see, math can be done within the curly brackets while using f-strings
# The rounding function allows for the limiting of decimal places while using
# the float type. In this case, limiting to two decimal places