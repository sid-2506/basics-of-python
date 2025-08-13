# Concession Stand program

menu = {
    "Hot Dog": 5.00,
    "Popcorn": 3.50,
    "Soda": 2.00,
    "Candy": 1.50,
    "Pizza": 6.00,
    "Nachos": 4.00,
    "Ice Cream": 2.50,
    "Pretzel": 3.00,
    "Chips": 1.00,
    "Fries": 2.00
}

cart = []

total = 0.0

for key,value in menu.items():
    print(f"{key}: ${value:.2f}")
    
while True:
    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    elif menu.get(food):
        cart.append(food)
        total += menu[food]
        print(f"Added {food} to cart. Total: ${total:.2f}")
    else:
        print("Invalid food item.")
        
print(f"Your bill is :  {total:.2f}")