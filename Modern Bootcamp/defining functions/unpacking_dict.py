# Unpacking - Dictionary

# Same concept as unpacking Tuples and Lists
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

display_names(names) 
# This will not work to pass the dictionary to the def funtion

display_names(**names)  
# It requires the use of double asterisks "**"

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7
