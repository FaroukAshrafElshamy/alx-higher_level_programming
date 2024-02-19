#!/usr/bin/python3
""" MyList class inherit from list class """


class MyList(list):
    """Print sorted array"""
    def print_sorted(self):

        print(sorted(self))
