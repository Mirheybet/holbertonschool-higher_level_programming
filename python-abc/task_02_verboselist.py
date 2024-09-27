#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
abstract
"""


class VerboseList(list):
    """
    child from builtin list class
    """

    def append(self, value):
        """
        add
        """
        print("Added [{}] to the list.".format(value))
        super().append(value)

    def extend(self, value):
        """
        len
        """
        print("Extended the list with [{}] items.".format(len(value)))
        super().extend(value)

    def remove(self, value):
        """
        del
        """
        if value in self:
            print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, value=None):
        """
        ded last
        """

        if value is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
            return item
        else:
            item = super().pop(value)
            print("Popped [{}] from the list.".format(item))
            return item
