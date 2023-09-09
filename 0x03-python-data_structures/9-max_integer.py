#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        idx = len(my_list) - 1
        i = 1
        highest = my_list[0]
        while i <= idx:
            if highest <= my_list[i]:
                highest = my_list[i]

            i += 1

        return (highest)
