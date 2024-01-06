#!/usr/bin/python3
'''
 takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
'''
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
    else:
        url = argv[1]
        try:
            with urlopen(url) as response:
                decoded = response.read().decode('utf-8')
                print(decoded)
        except HTTPError as e:
            print("Error code: {}".format(e.code))
