#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_list = []
    total_sum = 0
    for num in my_list:
        if num not in unique_list:
            total_sum += num
            unique_list.append(num)
    return total_sum
