#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = -number % 10
    last = -last
else:
    last = number % 10

if last > 5:
    string_print = "and is greater than 5"
elif last == 0:
    string_print = "and is 0"
else:
    string_print = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last, string_print))
