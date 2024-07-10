#!/usr/bin/python3
"""def square"""


class Square:
    """Definition of 'Square' class with private instance attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Represents a square with a specified size and position.

        Args:
            size (int): The side length of the square.
            position (tuple): The position of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 \
           or not all(isinstance(i, int) for i in position) \
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size attribute of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square using '#' characters."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Getter for position attribute of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute of the square."""
        if isinstance(value, tuple) and len(value) == 2 \
           and isinstance(value[0], int) and isinstance(value[1], int) \
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
