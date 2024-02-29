#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    LD = number % -10

else:
    LD = number % 10

if LD > 5:
    print(f"Last digit of {number} is {LD} and is greater than 5")
elif LD < 6 and LD != 0:
    print(f"Last digit of {number} is {LD} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {LD} and is 0")
