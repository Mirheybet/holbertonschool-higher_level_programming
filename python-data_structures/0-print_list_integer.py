#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if (my_list == []):
        return None
    for i in my_list:
        print("{:d}".format(i), end="\n")
