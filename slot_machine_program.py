# Slot Machine (Like a game)
import random
import time

balance = 100
symbols = ['👩🏽','👨🏽','🧑🏽','👧🏽','👦🏽']

def spin(amount):
    global symbols
    global balance
    
    print("Checking balance",end="")
    for i in range(5):
        print(".",end="")
        time.sleep(1)
    print()
    if amount>balance:
        print("You don't have sufficient balance")
        return
    
    allSym = []
    
    print("Starting",end="")
    for i in range(4):
        print('.',end="")
    print()
    
    for i in range(3):
        time.sleep(1)
        sym = random.choice(symbols)
        print(sym,end=" - ")
        allSym.append(sym)
    print()
    
    print("Analysing",end="")
    for i in range(5):
        print(".",end="")
        time.sleep(1)
    time.sleep(1)
    print()
    print("Result ",end="")
    if allSym[0]==allSym[1] and allSym[1]==allSym[2]:
        print("You won!")
        if allSym[0] == '👩🏽':
            amount *= 2
        elif allSym[0] == '👨🏽':
            amount *= 3
        elif allSym[0] == '🧑🏽':
            amount *= 4
        elif allSym[0] == '👧🏽':
            amount *= 5
        elif allSym[0] == '👦🏽':
            amount *= 6
        print(f"{amount}$ credited to your account")
        balance+=amount
    else:
        print("You lost!")
        balance-=amount
        
def seeBalance():
    global balance
    time.sleep(1)
    print(f"Your balance is : {balance}")      

while True:
    print("Welcome to Slot machine game")
    print('👩🏽,👨🏽,🧑🏽,👧🏽,👦🏽')
    print("1.Spin")
    print("2.See balance")
    print("3.Quit")
    choice = input("Select option (1,2,3) : ")
    
    match (choice):
        case '1':
            amount = float(input("Enter bet amount : "))
            if amount<0:
                print("Amount should be greater than zero")
                print()
                continue
            spin(amount)
            time.sleep(1)
            print()
        case '2':
            seeBalance()
            time.sleep(1)
            print()
        case '3':
            print("Logging out",end="")
            for i in range(5):
                print(".",end="")
                time.sleep(1)
            time.sleep(2)
            print()
            print("Signed out!")
            print("Thank you for using our app!")
            break
        case _:
            print("Invalid choice! Please try again.")
            time.sleep(2)
            print()
    if balance==0:
        print("Game over!\nBalance is 0")
        print("Logging out",end="")
        for i in range(5):
            print(".",end="")
            time.sleep(1)
        time.sleep(2)
        print()
        print("Signed out!")
        print("Thank you for using our app!")
        break