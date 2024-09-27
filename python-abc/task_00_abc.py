#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""
abstraction
"""


class Animal(ABC):
    """
    dont use this class
    """
    @abstractmethod
    def sound(self):
        """
        sound
        """
        pass


class Dog(Animal):
    """
    child from Animal
    """
    def sound(self):
        """
        "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    child from Animal
    """
    def sound(self):
        """
        "Meow"
        """
        return "Meow"
