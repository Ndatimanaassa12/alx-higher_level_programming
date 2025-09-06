#!/usr/bin/python3
"""Defines a function that returns a dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization.
    
    Args:
        obj: An instance of a class.
    
    Returns:
        dict: A dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__

