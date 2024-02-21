#!/usr/bin/python3
""" A function that takes a file """
import json


def load_from_json_file(filename):
    """ Create a Python object from a JSON file """
    with open(filename) as File:
        return json.load(File)
