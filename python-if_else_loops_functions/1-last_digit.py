#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
posetive = abs(number)
if (posetive%10 == 0):
    print(f"Last digit of {number} is 0 and is 0")

elif (number < 0):
     posetive = (posetive % 10) * (-1)
     print(f"Last digit of {number} is {posetive} and is less than 6 and not 0")

elif (number > 0):
    posetive = (posetive % 10)
    if (posetive > 5):
        print(f"Last digit of {number} is {posetive} and is greater than 5")
    elif (posetive < 6):
        print(f"Last digit of {number} is {posetive} and is less than 6 and not 0")
