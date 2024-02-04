#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string != "" or roman_string != None:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        outnum = 0
        for i in roman_string:
            outnum += rom[i]
        return outnum
    else:
        return None
