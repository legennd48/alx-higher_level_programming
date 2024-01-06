#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the
 passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''
from urllib.request import Request, urlopen
from sys import argv
from urllib.parse import urlencode


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
    else:
        url = argv[1]
        email = {'email': argv[2]}
        data = urlencode(email).encode('ascii')
        req = Request(url, data)

        with urlopen(req) as response:
            decoded = response.read().decode('utf-8')
            print(decoded)
