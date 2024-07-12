#!/usr/bin/python3
"""Defines a inherits_from() function"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
