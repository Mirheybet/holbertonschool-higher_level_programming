#!/usr/bin/python3
"""
This module provides a function `add_integer(a, b=98)` that adds two integers.
It handles both integer and float inputs by casting floats to integers.
Raises TypeError if either argument is not an integer or a float.
"""

def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
