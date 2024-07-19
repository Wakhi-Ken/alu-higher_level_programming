#!/usr/bin/python3
"""class_to_json function."""


def class_to_json(obj):
    """Gets the dictionary description of an object
    """
    return obj.__dict__
