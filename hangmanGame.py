import random

words = ["india", "france", "germany", "italy", "spain", "portugal", "england", "australia", "canada"]

hangman_stages = {
    0: """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |
       """,
    1: """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |
       """,
    2: """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |
       """,
    3: """
       --------
       |      |
       |      O
       |     /|
       |      
       |
       """,
    4: """
       --------
       |      |
       |      O
       |      |
       |      
       |
       """,
    5: """
       --------
       |      |
       |      O
       |      
       |      
       |
       """,
    6: """
       --------
       |      
       |      
       |      
       |      
       |
       """
}

def show_hangman(stage):
    print(hangman_stages[stage])

def show_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    print("Word:", displayed_word.strip())

def play_game():
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    
    while True:
        show_hangman(wrong_guesses)
        show_word(word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong!")

        if set(word) <= guessed_letters:
            show_hangman(wrong_guesses)
            print("🎉 Congratulations! You guessed the word:", word)
            break

        if wrong_guesses == max_wrong:
            show_hangman(wrong_guesses)
            print("💀 Game Over! The word was:", word)
            break

play_game()
