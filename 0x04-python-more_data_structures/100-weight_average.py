#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    weighted_sum = 0
    total_weight = 0

    for tuple_item in my_list:
        weighted_sum += tuple_item[0] * tuple_item[1]
        total_weight += tuple_item[1]

    if total_weight == 0:
        return (0)

    return (weighted_sum / total_weight)
