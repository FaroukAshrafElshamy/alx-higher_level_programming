#!/usr/bin/python3
import json
""" A function that takes a file """


def to_json_string(my_obj):
    """ Returns json representation of a string """
    return json.dump(my_obj)
