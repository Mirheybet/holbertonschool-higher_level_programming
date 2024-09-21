#!/usr/bin/python3
"""
an empty class Rectangle
"""


class Rectangle:
    """
    an empty class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        main instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width
        """
        return self.__width

    @property
    def height(self):
        """
        Height
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width mus be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mus be >= 0")
        self.__height = value
