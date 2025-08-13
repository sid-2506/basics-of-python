# Rock Paper Scissors

import random

options = ["rock", "paper", "scissors"]

computer_score = 0
player_score = 0

rounds = int(input("Enter number of rounds to play: "))

for i in range(rounds):
    computer =  random.choice(options)
    player = input("Enter your choice (rock, paper, scissors): ").lower()
    
    while player not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    if player == computer:
        print(f"Round {i+1}: It's a tie! Both chose {player}.")
    elif ((player == "rock" or player == "paper") and (computer == "paper" or computer == "rock")):
        print("Paper covers rock")
        winner = "computer" if player == "rock" else "player"
        print(f"Round {i+1}: {winner.capitalize()} wins!")
        if winner == "computer":
            computer_score += 1
        else:
            player_score += 1
    elif ((player == "paper" or player == "scissors") and (computer == "scissors" or computer == "paper")):
        print("Scissors cut paper")
        winner = "computer" if player == "paper" else "player"
        print(f"Round {i+1}: {winner.capitalize()} wins!")
        if winner == "computer":
            computer_score += 1
        else:
            player_score += 1   
    elif ((player == "rock" or player == "scissors") and (computer == "scissors" or computer == "rock")):
        print("Rock crushes scissors")
        winner = "computer" if computer == "rock" else "player"
        print(f"Round {i+1}: {winner.capitalize()} wins!")
        if winner == "computer":
            computer_score += 1
        else:
            player_score += 1
    print(f"Score: Player {player_score} - Computer {computer_score}\n")
    
if computer_score > player_score:
    print("Computer wins the game!")
elif player_score > computer_score:
    print("Player wins the game!")
else:
    print("The game is a tie!")