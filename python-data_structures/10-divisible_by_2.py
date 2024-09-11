#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    dvd_by_2 = []
    for i in my_list:
        if (i % 2 == 0):
            dvd_by_2.append(True)
        else:
            dvd_by_2.append(False)
    return (dvd_by_2)
