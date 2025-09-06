#!/usr/bin/python3
"""Defines a Student class with selective JSON representation."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include. If None, include all.

        Returns:
            dict: Dictionary of selected or all instance attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            # Include only attributes that exist in the instance
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # If attrs is None or not a list, return all attributes
        return self.__dict__

