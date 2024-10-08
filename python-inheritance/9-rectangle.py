#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class two private attributes"""
    def __init__(self, width, height):
        """sets width and height private attributes."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """description of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
