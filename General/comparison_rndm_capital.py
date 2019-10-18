print("Let's play rock, paper, scissors!").lower()

import random

player = input("select: rock, paper or scissors: ")

rand_num = random.randint(0,2)
computer = 0

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print("Computer selected: " + computer)
print("You chose: " + player)
if player == computer:
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("You lose!")
    elif computer == "scissors":
        print("You win!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    elif computer == "rock":
        print("You lose!")
elif player == "paper":
    if computer == "scissors":
        print("You lose!")
    if computer == "rock":
        print("You win!")
else:
    print("Please only enter rock, paper or scissors")



