#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        temp = list(a_dictionary.values())
        temp2 = list(a_dictionary.keys())
        item = temp.index(max(temp))
        return temp2[item]
