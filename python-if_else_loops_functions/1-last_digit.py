#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
posetive = abs(number)
if(posetive%10 == 0):
    print(f"Last digit of {number} is 0 and is 0")
elif(posetive%10 > 5):
    if(number<0):
        posetive=(posetive%10)*(-1)
        print(f"Last digit of {number} is {posetive} and is greater than 5")
    else:
        print(f"Last digit of {number} is {posetive%10} and is greater than 5")
else:
    if(number<0):
        posetive=(posetive%10)*(-1)
        print(f"Last digit of {number} is {posetive} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {posetive%10} and is less than 6 and not 0")
