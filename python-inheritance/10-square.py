#!/usr/bin/python3
"""Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle."""
    def __init__(self, size):
        """Init width and height to size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
