#!/usr/bin/python3
""" Read from a file using with statement """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as File:
        print(File.read(), end='')
