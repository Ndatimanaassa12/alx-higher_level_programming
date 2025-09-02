#!/usr/bin/python3
"""
Module that contains the function `lookup`.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attributes and methods available in the object.
    """
    return dir(obj)

