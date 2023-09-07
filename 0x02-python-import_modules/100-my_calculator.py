#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    av = sys.argv
    ac = len(av) - 1

    if ac != 3:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    else:
        a = int(av[1])
        op = av[2]
        b = int(av[3])

        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))

        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))

        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))

        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))

        else:
            unknown = "Unknown operator. Available operators: +, -, * and /"
            print("{}".format(unknown))
            exit(1)
