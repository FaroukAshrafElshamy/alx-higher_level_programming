#!/usr/bin/python3
""" Type checking function """


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
