# Simple calculator

num1 = float(input("Enter first number : "))
operator = input("Enter an operator(+,-,/,*) : ")
num2 = float(input("Enter second number : "))

if operator=="+":
    print(f"Sum = {num1+num2}")
elif operator=="-":
    print(f"Division = {num1-num2}")
elif operator=="/":
    print(f"Division = {num1/num2}")
elif operator=="*":
    print(f"Product = {num1*num2}")
else :
    print("Invalid Operator")