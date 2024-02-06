#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    List = ''
    while i < x:
        try:
            List += str(my_list[i])
            i += 1
        except IndexError:
            break
    if List != '':
        print(int(List))
    return i
