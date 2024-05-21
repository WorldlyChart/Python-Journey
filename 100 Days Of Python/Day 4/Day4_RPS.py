import random

choices = ["rock", "paper", "scissors"]


player = int(input("Rock, Paper, Scissors, Shoot! \n choose 0 for rock, 1, for paper, and 2 for scissors\n"))
computer = random.randint(0,2)
if player > 2:
    print("you typed an invalid number, try again")

print(f"You chose {choices[player]}.\nThe computer chose {choices[computer]}.")
if player == 0:
    if computer == 0:
        print("Its a Draw!")
    if computer == 1:
        print("You Lose!")
    if computer == 2:
        print("You Win!")
elif player == 1:
    if computer == 0:
        print("You Win!")
    if computer == 1:
        print("Its a Draw!")
    if computer == 2:
        print("You Lose!")
elif player == 2:
    if computer == 0:
        print("You Lose!")
    if computer == 1:
        print("You Win!")
    if computer == 2:
        print("Its a Draw!")
else:
    print("you typed an invalid number, try again")
