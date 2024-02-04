#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    else:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        outnum = 0
        for i in roman_string:
            if roman_string not in ["IV","IX"]:
                outnum += rom[i]
            else:
                if i == "IV":
                    outnum = 4
                else:
                    outnum = 9
        return outnum
