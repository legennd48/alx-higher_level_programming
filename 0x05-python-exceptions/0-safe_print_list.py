#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    n = 0
    while (n < x):
        try:
            print("{}".format(my_liat[n]), end="")
            n += 1

        except IndexError:
            break

    print()
    return (n)
