# Python Quiz

questions = (
    "How many elements are in periodic table?",
    "What is the capital of France?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?"
)

options = (
    ("A. 116","B. 117","C. 118","D. 119"),
    ("A. Berlin","B. Madrid","C. Paris","D. Rome"),
    ("A. Harper Lee","B. Mark Twain","C. J.K. Rowling","D. Ernest Hemingway"),
    ("A. Earth","B. Jupiter","C. Mars","D. Saturn"),
    ("A. Au","B. Ag","C. Pb","D. Fe")
)

answers = (
    "C",
    "C",
    "A",
    "B",
    "A"
)

guesses = []
score = 0

for i in range(len(questions)):
    print(f"Question {i+1}: {questions[i]}")
    for j in options[i]:
        print(j)
    guess = input("Select your answer (a,b,c,d): ").upper()
    guesses.append(guess)
    if guess==answers[i]:
        print("CORRECT!")
        score+=1
    else:
        print("INCORRECT!")
        print("Correct answer is "+answers[i])
        print("Your answer was: "+guesses[i])
    print()

print(f"Your score is {score/len(questions)*100:.2f}%")