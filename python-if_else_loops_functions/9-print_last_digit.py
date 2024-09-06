#!/usr/bin/python3
def print_last_digit(number):
    nmb_clone = abs(number)
    if (number < 0):
        return (nmb_clone % 10)
    return (number % 10)
