#!/usr/bin/python3
"""Defines a MyList subclass."""


class MyList(list):
    """A subclass print_sorted method"""

    def print_sorted(self):
        """sorted in ascending order"""
        print(sorted(self))
