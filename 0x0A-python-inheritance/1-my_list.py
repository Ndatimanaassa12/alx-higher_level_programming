#!/usr/bin/python3
"""
Module that defines the class MyList.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))

