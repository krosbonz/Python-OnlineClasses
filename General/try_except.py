try:
    some_code
except #optional error type:
    print('this code is garbage')


# This will only provide error information if the error matches
# the error type
try:
    some_code
except NameError:
    print('you screwed up your code')


# String multiple error types together with tuple
try:
    some_code
except (NameError, TypeError):
    print('you screwed up your code')

# Or use multiple "excepts"
try:
    some_code
except NameError:
    print('name error!')
except TypeError:
    print('type error!')



# This will return "None" instead of custom message
try:
    some_code
except NameError:
    return None

try:
    num = int(input("Enter a number"))
except:
    print("Not a number")
# Error msg if not an integer
else:
    print("Good number!")
# Else will run when "except" does not
finally:
    print("If you screwed up try again... or good job")
# Finally runs no matter what


# Continue to loop until "else" break
while true:
    try:
        num = int(input("Enter a number"))
    except:
        print("Not a number")
    else:
        print("Good number!")
        break
        # A proper response was received so you want to break the loop
    finally:
        print("If you screwed up try again... or good job")
print("This is where more code would run")
# Once the loop breaks the next line of code would run

