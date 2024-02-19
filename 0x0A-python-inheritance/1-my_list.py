#!/usr/bin/python3
""" MyList class inherit from list class """


class MyList(list):
    """Print sorted array"""
    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
