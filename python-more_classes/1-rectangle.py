#!/usr/bin/python3
"""defines a rectangle by (based on 0-rectangle.py)"""


class Rectangle:
    """ defines a rectangle by: (based on 0-rectangle.py"""
    def __init__(self, width=0, height=0):
        """ defines a rectangle by: (based on 0-rectangle.py"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
