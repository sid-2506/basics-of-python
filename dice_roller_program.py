# Dice roller program

# ● ┌ ─ ┐ │ └ ┘
import random
dices = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
        ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
   4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
   5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
   6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

total = 0
rolls = int(input("How many times do you want to roll the dice? "))

for i in range(rolls):
    roll = random.randint(1, 6)
    print(dices[roll][0])
    print(dices[roll][1])
    print(dices[roll][2])
    print(dices[roll][3])
    print(dices[roll][4])
    total += roll

print(f"Total: {total}")