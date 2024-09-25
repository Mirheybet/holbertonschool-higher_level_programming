#!/usr/bin/python3
"""
bitwise
"""


class MyInt(int):
    """
    MyInt
    """

    def __eq__(self, value):
        """
        ==
        """
        return self.real != value

    def __ne__(self, value):
        """
        !=
        """
        return self.real == value
