#!/usr/bin/python3
""" Type checking function """


def is_same_class(obj, a_class):
    """ Check the object """
    if type(obj) == a_class:
        return True
    else:
        return False
