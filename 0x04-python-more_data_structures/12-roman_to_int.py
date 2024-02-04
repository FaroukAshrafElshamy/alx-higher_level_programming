#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    else:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        outnum = 0
        for i in roman_string:
            if rom.get(i, 0) == 0:
                return 0
            if outnum > 0 and outnum < rom[i]:
                outnum = rom[i] - outnum
            else:
                outnum += rom[i]
        return outnum
