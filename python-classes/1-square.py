#!/usr/bin/python3
"""Definition  a  Square' class _ private instance attribute"""


class Square:
    """Definition of -Square'"""
    def __init__(self, size=0):
        """Inits Square with 'size' private instance attribute

            Args:
                size: An integer size of the square.
        """
        self.__size = size
