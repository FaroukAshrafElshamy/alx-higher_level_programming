#!/usr/bin/python3

def common_elements(set_1, set_2):
    out = set()
    for i in set_1:
        if i in set_2:
            out.add(i)
    for z in set_2:
        if z in set_1:
            out.add(z)
    return out
