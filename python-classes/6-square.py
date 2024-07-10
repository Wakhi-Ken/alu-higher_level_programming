#!/usr/bin/python3
""" def of a square"""


class Square:
    """Definition of 'Square' class with private instance attribute."""

    def __init__(self, size=0, position=(0, 0)):
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
        if isinstance(value, tuple) and type(value) == int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
