#!/usr/bin/python3

def print_last_digit(number):
    if number > 10:
        print("{}".format(number % 10), end='')
    else:
        print("{}".format(number), end='')
