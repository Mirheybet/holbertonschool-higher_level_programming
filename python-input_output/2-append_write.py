#!/usr/bin/python3
"""
append
"""


def append_write(filename="", text=""):
    """
    with
    """
    with open(filename, "a", encoding='utf-8') as file:
        file = file.write(text)
        return file
