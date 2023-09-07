#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv) - 1

    if num <= 1:
        print("{:d}".format(0 if num == 0 else int(argv[1])))

    else:
        sum = 0
        i = 1
        while i <= num:
            sum += int(argv[i])
            i += 1

    print("{:d}".format(sum))
