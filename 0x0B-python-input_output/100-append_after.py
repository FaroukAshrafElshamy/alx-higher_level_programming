#!/usr/bin/python3
""" A function that takes a file """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a specific string """
    text = ""
    with open(filename) as File:
        for line in File:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as Write:
        Write.write(text)
