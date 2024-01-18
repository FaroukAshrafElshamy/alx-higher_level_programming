#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        n = 1
        print("{} arguments.".format(len(sys.argv)-1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(n, sys.argv[i]))
            n += 1
    else:
        print("0 arguments.")
