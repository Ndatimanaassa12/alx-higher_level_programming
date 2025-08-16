#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize a new Square with given size (no type/value check)."""
        self.__size = size

