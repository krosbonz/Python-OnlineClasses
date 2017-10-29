score = input("Enter score: ")
try:
    scr = float(score)
except:
    print("Please enter number between 0 and 1")
    quit()
if scr > 1:
    print("Please enter number between 0 and 1")
    quit()
elif scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
elif scr < 0.6:
    print("F")
else:
    quit()