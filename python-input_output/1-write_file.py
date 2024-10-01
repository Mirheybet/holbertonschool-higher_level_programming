#!/usr/bin/python3
"""
write
"""


def write_file(filename="", text=""):
    """
    overwrite
    """
    with open(filename, "w", encoding='utf-8') as file:
        file = file.write(text)
        return file
