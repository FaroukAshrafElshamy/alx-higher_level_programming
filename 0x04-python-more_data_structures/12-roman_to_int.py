#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    outnum = 0
    for i in roman_string:
        if outnum > 0 and outnum < rom[i]:
            outnum = rom[i] - outnum
        else:
            outnum += rom[i]
    return outnum
