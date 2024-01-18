#!/usr/bin/python3
from sys import *
if len(argv) > 1:
    n = 1
    for i in range(1, len(argv)):
        print("{}: {}".format(n, argv[i]))
        n += 1
else:
    print("0 arguments.")
