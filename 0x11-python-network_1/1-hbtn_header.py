#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
'''
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        url = argv[1]
        with urlopen(url) as response:
            x_id = response.info().get('X-Request-Id')
            print("{}".format(x_id))
