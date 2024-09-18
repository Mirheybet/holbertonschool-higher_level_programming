#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """
    Write a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):

        """
        size must be an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """
        size must be >= 0
        """
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.__size = self.__size ** 2
        return self.__size
