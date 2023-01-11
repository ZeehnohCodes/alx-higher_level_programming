#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def _init_(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super()._init_(size, size)
        self.__size = size
