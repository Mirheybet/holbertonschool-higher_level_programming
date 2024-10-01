#!/usr/bin/python
"""
append
"""


def append_write(filename="", text=""):
    """
    with
    """
    with open("file_append.txt", "a", encoding='utf-8') as file:
        file = file.write(text)
        return file
