#!/usr/bin/python3
""" A function that takes a file name """


def read_file(filename=""):
    """ Read from a file using with statement """
    with open(filename, encoding="utf-8") as File:
        print(File.read(), end='')
