# Weight Converter

weight = float(input("Enter weight : "))
unit = input("Unit (lbs/kgs): ")

if unit == "lbs":
    print(f"Weight in kgs: {weight /2.20462}")
elif unit == "kgs":
    print(f"Weight in lbs: {weight * 2.20462}")
else:
    print("Invalid unit")
