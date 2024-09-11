#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_my_list = [i for i in my_list]
    if (idx < 0 or idx > len(my_list)):
        return cp_my_list
    cp_my_list = [i for i in my_list]
    cp_my_list[idx] = element
    return (cp_my_list)
