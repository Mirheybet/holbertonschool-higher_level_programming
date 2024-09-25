#!/usr/bin/python3
"""
check subclass
"""


def inherits_from(obj, a_class):
    """
    issubclass
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
