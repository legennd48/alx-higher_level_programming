#!/usr/bin/python3


def uppercase(str):
    upper = ""
    for i in str:
        if 'a' <= i <= 'z':
            upper += chr(ord(i) - 32)

        else:
            upper += i

    print(upper)
