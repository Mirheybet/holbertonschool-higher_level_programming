#!/usr/bin/env python 3
"""
counter
"""


class CountedIterator:
    """
    counter
    """

    def __init__(self, iterable):
        """
        iterable
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        next
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Counter
        """
        return self.counter
