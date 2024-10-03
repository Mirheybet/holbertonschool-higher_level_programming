#!/usr/bin/python3
"""
student
"""


class Student:
    """
    __init__
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    json for class
    """
    def to_json(self, attrs=None):
        if (isinstance(attrs, list) and
                all(isinstance(att, str) for att in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
