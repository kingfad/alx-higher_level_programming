#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    no_arg = len(sys.argv)
    for i in range(1, no_arg):
        sum += int(sys.argv[i])
    print("{}".format(sum))
