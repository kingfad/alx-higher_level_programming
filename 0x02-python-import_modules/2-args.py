#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_arg = len(sys.argv) - 1
    if no_arg == 1:
        print("{} argument.".format(no_arg))
    else:
        print("{} arguments:".format(no_arg))
    for i in range(1, no_arg + 1):
        print("{}: {}".format(i, sys.argv[i]))
