#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square():
    """
    Write a class Square that defines a square by: (based on 1-square.py)
    """
    def __init__(self, size=0):
        """
        errorhandling: size must be an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """
        errorhandling: size must be >= 0
        """
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
