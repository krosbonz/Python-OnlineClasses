# To enter you must be at least 18. To drink you must be at least 21

age = input("How old are you?: ")
if age != "":
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but you can't drink")
    elif int(age) >= 21:
        print("You may enter and drink")
    else: 
        print("No bueno, no enter")
else:
    print("Please enter a real age or buzz off")

# You could also use;
# age = int(age) before the nested "if"

# Another option for the first "if";
# if age and (age >= 18 and age < 21):
# This would do away with the nested conditional

# The simplest code to cover all requirements;

age = input("How old are you?: ")
if age:
    age = int(age)
    if age >= 21:
        print("You may enter and drink")
    elif age >= 18:
        print("You may enter, but not drink")
    else:
        print("No bueno")
else: 
    print("Please enter an age")

# This works because the first "if" takes care of all over 21 ages, so 
# if the age entered is less than 21 it will bounce down to the next line
# in the conditional