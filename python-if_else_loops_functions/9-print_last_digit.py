#!/usr/bin/python3
def print_last_digit(number):
    nmb_clone = abs(number)
    if (number < 0):
        print("{}".format(nmb_clone % 10), end = "")
        return (nmb_clone % 10)
    print("{}".format(nmb_clone % 10), end = "")
    return (number % 10)
