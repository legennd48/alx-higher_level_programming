#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    n = 0

    while (n < x):
        try:
            if (my_list[n].isdigit()):
                print("{:d}".format(my_list[n]))

            else:
                continue

        except IndexError:
            break

        n += 1
