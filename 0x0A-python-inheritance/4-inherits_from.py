#!/usr/bin/python3
""" Define a function """


def inherits_from(obj, a_class):
    """ instance of a class that inherited """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
