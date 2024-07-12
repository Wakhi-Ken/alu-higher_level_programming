#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """with an integer_validation method."""
    def area(self):
        """Unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
