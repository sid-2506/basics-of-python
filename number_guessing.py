# Number guessing game

import random

number = random.randint(1,101)
guesses = 0

while True:
    guesses+=1
    guess = int(input("Enter your guess : "))
    if(guess<1 or guess>100):
        print("Out of range!")
        print("Guess the number from 1 to 100")
    elif guess>number:
        print("Actual number is smaller than your guess")
        print("Try again")
    elif guess<number:
        print("Actual number is greater than your guess")
        print("Try again")
    elif guess==number:
        print("Spot on!")
        print(f"You took {guesses} chances")
        break
    