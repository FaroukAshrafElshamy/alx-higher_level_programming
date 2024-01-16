#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LD = int(str(number)[-1])
if number < 0:
    LD = -LD
if LD > 5:
    print(f"Last digit of {number} is {LD} and is greater than 5")
elif LD < 6 and LD != 0:
    print(f"Last digit of {number} is {LD} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {LD} and is 0")
