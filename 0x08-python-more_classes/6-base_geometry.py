#!/usr/bin/python3
"""
Module that defines the class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area() method.
    """

    def area(self):
        """
        Raises an exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

