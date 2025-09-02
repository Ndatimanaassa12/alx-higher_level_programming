#!/usr/bin/python3
"""
Module that defines the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of a_class or
    an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
              otherwise False.
    """
    return isinstance(obj, a_class)

