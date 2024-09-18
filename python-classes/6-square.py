#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """
    Write a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):

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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """
        size must be >= 0
        """
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        if size is equal to 0, print an empty line
        """
        if (self.__size == 0):
            print()
        """
        hat prints in stdout the square with the character #
        """
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
