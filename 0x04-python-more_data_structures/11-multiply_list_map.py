#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    temp = my_list.copy()
    return list(map(lambda x: x*number, temp))
