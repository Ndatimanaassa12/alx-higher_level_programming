#!/usr/bin/python3
"""
Module that defines BaseGeometry with area() and integer_validator().
"""


class BaseGeometry:
    """
    BaseGeometry class that defines geometry operations.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the value (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

