#!/usr/bin/python3
"""Initilizing a new private inistance from Squalre class"""


class Square:
    """Initilization method"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            print("size must be an integer")
            raise TypeError

        elif size < 0:
            print("size must be >= 0")
            raise ValueError
