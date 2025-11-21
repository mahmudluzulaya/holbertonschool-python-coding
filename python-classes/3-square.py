#!/usr/bin/python3
"""Module that defines a Square class with size getter and setter."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
