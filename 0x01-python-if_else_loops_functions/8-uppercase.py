#!/usr/bin/python3
def uppercase(str):
    out = ''
    for char in str:
        if ord(char) > 90:
            out += chr(ord(char) + 32)
        else:
            out += char
    return out
