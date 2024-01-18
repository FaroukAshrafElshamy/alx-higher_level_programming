#!/usr/bin/python3
if __name__ == "__main__":
    import sys
z = len(sys.argv)
if z > 1:
    n = 1
    if z-1 == 1:
        print("{} argument:".format(z-1))
    else:
        print("{} arguments:".format(z-1))

    for i in range(1, z):
        print("{}: {}".format(n, sys.argv[i]))
        n += 1
else:
    print("0 arguments.")
