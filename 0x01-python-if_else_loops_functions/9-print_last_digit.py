#!/usr/bin/python3


def print_last_digit(number):
    num = number
    if num < 0:
        num *= -1

    last = num % 10
    print("{}".format(last), end="")
    return (last)
