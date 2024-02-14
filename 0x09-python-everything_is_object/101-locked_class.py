#!/usr/bin/python3
"""Defines a locked Class"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slot__ = ["first_name"]
