#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    avg, count = 0, 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        count += tup[1]
    return (avg / count)
