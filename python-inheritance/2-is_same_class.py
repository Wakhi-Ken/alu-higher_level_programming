#!/usr/bin/python3
"""Defines is_same_class() function"""


def is_same_class(obj, a_class):
    """Checks of object then reuturns True if the object is an exact instance or False"""
    return type(obj) == a_class
