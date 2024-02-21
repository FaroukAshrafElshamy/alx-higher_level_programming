#!/usr/bin/python3
""" A function that takes a file """


def append_write(filename="", text=""):
    """ Append text to the file """
    with open(filename, 'a', encoding="utf-8") as File:
        return File.write(text)
