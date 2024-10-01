#!/usr/bin/python3
"""
read_file
"""


def read_file(filename=""):
    """
    read file utf-8
    """

    with open("my_file_0.txt", encoding='utf-8') as file:
        file = file.read()
        print(file, end="")
