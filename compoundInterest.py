# Compound interest calculator

principle = 0
rate = 0
time = 0

while principle<=0:
    principle = float(input("Enter principle amount : "))
    if(principle<=0):
        print("Principle should not be negative or zero")
        
while rate<=0:
    rate = float(input("Enter rate of interest : "))
    if(rate<=0):
        print("Rate of interest should not be negative or zero")
        
while time<=0:
    time = float(input("Enter time (in years) : "))
    if(time<=0):
        print("Time should not be negative or zero")
        
interest = (principle*pow((1+rate/100),time))-principle

print(f"According to the calculations,(principle = {principle}, rate = {rate}, time = {time}) the compound interest is: {interest:.2f}")