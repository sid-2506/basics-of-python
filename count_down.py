# Count down
import time

seconds = int(input("Enter the number of seconds to count down from: "))

for i in reversed(range(1,seconds + 1)):
    time.sleep(1)
    seconds = i%60
    minutes = int(i/60)%60
    hours = int(i/3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Boom!")
time.sleep(1)
print("Time's up!")