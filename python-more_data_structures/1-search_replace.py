#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_my_list = my_list
    for i in range(len(cp_my_list)):
        if cp_my_list[i] == search:
            cp_my_list[i] = replace
    return (cp_my_list)
