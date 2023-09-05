#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    num *= -1

last = num % 10
print("Last digit of {} is {}".format(number, last), end="")
if last > 5:
    print(" and is greater than 5", end="")

elif last == 0:
    print(" and is 0", end="")

if last < 6 and last != 0:
    print(" and is less than 6 and not 0", end="")

print()
