#!/usr/bin/python3
""" A function that takes a file """
import json


def from_json_string(my_str):
    """Return a Python object that represents a JSON string """
    return json.loads(my_str)
