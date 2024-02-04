#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    temp = a_dictionary.copy()
    temp.pop(key)
    return temp
