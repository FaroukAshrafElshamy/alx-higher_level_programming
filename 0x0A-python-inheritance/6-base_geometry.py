#!/usr/bin/python3
"""Defines an empty class """


class BaseGeometry:
    """Represent base geometry"""
    def area(self):
        raise Exception("area() is not implemented")
