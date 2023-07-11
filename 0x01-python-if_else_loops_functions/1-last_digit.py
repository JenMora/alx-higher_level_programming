#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_int = abs(number) % 10
if number < 0:
    last_int = -last_int
    print(f"Last digit of {number:d} is {last_int:d} and is ", end="")
    if last_num > 5:
        print("greater than 5")
    elif last_int == 0:
        print("0")
    else:
        print("less than 6 and not 0")
