#!/usr/bin/python3
"""Def 'Square' class with a private instance attribute"""


class Square:
    """Definition of 'Square'"""
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
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates area of square"""
        return self.__size ** 2
     
    @property
    def size(self):
        """size of the square

        Returns:
            size_attribute of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size with a value

        Args:
            value: value to assign to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
