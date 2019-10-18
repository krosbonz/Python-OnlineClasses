import random

randnum = random.randint(1,10)

# My attempt is from line 1 to 24 (uncomment line 7) and it works!
# The corrected way is from line 28-42, including "import" and "randnum"

guessnum = int(input("Guess a number between 1 and 10: "))

while True:
    while guessnum != randnum:
        if guessnum < randnum:
            print("Too low!")
            guessnum = int(input("Guess a number between 1 and 10: "))
        else: 
            print("Too high!")
            guessnum = int(input("Guess a number between 1 and 10: "))
    print("You win!")
    playagain = input("Want to play again? y/n ")
    if playagain == "y":
        randnum = random.randint(1,10)
        guessnum = int(input("Guess a number between 1 and 10: "))
    else:
        print("Thanks for playing!")
        break

    

while True:
    guessnum = int(input("Guess a number between 1 and 10: "))
    if guessnum > randnum:
        print("Too high!")
    elif guessnum < randnum:
        print("Too low!")
    else:
        print("You win!")
        play = input("Do you wish to play again? (y/n) ")
        if play == "y":
            randnum = random.randint(1,10)
            guessnum = None
        else:
            print("Thanks for playing!")
            break



