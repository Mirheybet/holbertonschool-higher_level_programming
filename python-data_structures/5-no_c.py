#!/usr/bin/python3
def no_c(my_string):
    cp_my_list = [i for i in my_string if (i != 'c' and i != 'C')]
    cp_my_list = "".join(cp_my_list)
    return (cp_my_list)
