# Banking Application

import time

balance = 0.0

def deposit(amount):
    global balance
    print("Processing",end="")
    for i in range(5):
        print(".",end="")
        time.sleep(1)
    print()
    time.sleep(1)
    balance += amount
    print("Processed")
    time.sleep(1)
    print(f"Final balance : {balance}")
    

def withdraw(amount):
    global balance
    print("Checking balance",end="")
    for i in range(5):
        print(".",end="")
        time.sleep(1)
    print()
    if balance > amount:
        print("Amount available")
        print("Processing",end="")
        for i in range(5):
            print(".",end="")
            time.sleep(1)
        print()
        balance -= amount
        time.sleep(1)
        print("Processed")
        time.sleep(1)
        print(f"Final balance : {balance}")
    else:
        print("Amount unavailable!")
        

def showBalance():
    global balance
    time.sleep(1)
    print(f"Your balance is : {balance}")

while True:
    print("1.See Balance")
    print("2.deposit some amount")
    print("3.Withdraw some amount")
    print("4.Quit")
    choice = input("Choose what you want (1,2,3,4): ")
    
    match (choice):
        case '1':
            showBalance()
            print()
            time.sleep(2)
        case '2':
            amount = float(input("Enter amount to deposit : "))
            if(amount <= 0):
                print("Invalid amount! Please enter a positive number.")
                time.sleep(2)
                print()
                continue
            deposit(amount)
            print()
            time.sleep(2)
        case '3':
            amount = float(input("Enter amount to withdraw : "))
            if(amount <= 0):
                print("Invalid amount! Please enter a positive number.")
                time.sleep(2)
                print()
                continue
            withdraw(amount)
            print()
            time.sleep(2)
        case '4':
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