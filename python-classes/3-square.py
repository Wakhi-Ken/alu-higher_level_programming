#!/usr/bin/python3
"""Defines a class Square that defines a square by: (based on 2-square.py)"""
class Square:
    """Definition of a Square'"""
    def __init__(self, size=0):
        """
        Represents a square with a specified size.
        Args:
            size (int): The side length of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:

            raise ValueError("size must be >=0")
        self.size = size
        def area(self):
            """calculates the area of the squaew"""
            return self._size * self._size
