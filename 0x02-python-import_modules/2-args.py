#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv) - 1

    if num == 0:
        print("{} arguments.".format(0))

    else:
        print("{} {}:".format(num, "argument" if num == 1 else "arguments"))
        i = 1
        while i <= num:
            print("{}: {}".format(i, argv[i]))
            i += 1
