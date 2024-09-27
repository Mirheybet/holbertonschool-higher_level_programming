#!/usr/bin/env python3
from math import pi
from abc import ABC, abstractmethod
"""
abstract
"""


class Shape():
    """
    this class is asbtract
    """
    @abstractmethod
    def area(self):
        """
        for area
        """
        pass

    @abstractmethod
    def perimetr(self):
        """
        for perimetr
        """
        pass


"""
abstract
"""


class Circle(Shape):
    """
    child from Shape
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """
        3.14*R^2
        """
        return (pi * (self.radius**2))

    def perimeter(self):
        """
        2*3.14*R
        """
        return (pi * 2 * (self.radius))


class Rectangle(Shape):
    """
    child from Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        w*h
        """
        return self.width * self.height

    def perimeter(self):
        """
        2*(w+h)
        """
        return 2*(self.width + self.height)


def shape_info(obj):
    """
    func for info
    """
    area = obj.area()
    perimeter = obj.perimeter()

    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
