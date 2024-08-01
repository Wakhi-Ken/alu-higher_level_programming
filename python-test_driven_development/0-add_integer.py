#!/usr/bin/python3
"""Defines add_integer"""


def add_integer(a, b=98):
    """Calculates the sum of two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
