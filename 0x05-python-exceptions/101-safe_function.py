#!/usr/bin/python3
import sys


def safe_function(func, *args):
    try:
        r = func(*args)
        return r
    except Exception as error:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
