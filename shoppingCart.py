# Shopping Cart Program

foods = []
prices = []
pieces = []
total = 0.0

while True:
    food = input("Enter the food to buy (q to quit) : ")
    if food.lower() == 'q':
        break
    foods.append(food)
    price = float(input(f"Enter price of 1 {food} plate : "))
    piece = int(input(f"Enter how many {food}s you will buy : "))
    prices.append(price)
    pieces.append(piece)
    total += price * piece
    
print("Shopping cart summary")
for i in range(len(foods)):
    print(f"{pieces[i]} x {foods[i]} @ {prices[i]} = {prices[i] * pieces[i]:.2f}")
print(f"Total = {total:.2f}")