#!/usr/bin/python3
""" A function that takes a file """


def write_file(filename="", text=""):
    """ Write text into the file and overwrite its content """
    with open(filename, "w", encoding="utf-8") as File:
        return File.write(text)
