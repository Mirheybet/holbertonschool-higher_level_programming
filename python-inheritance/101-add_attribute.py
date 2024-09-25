#!/usr/bin/python3
"""
add_attribute
"""


def add_attribute(obj, att, value):
    """
    isdictionary
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
