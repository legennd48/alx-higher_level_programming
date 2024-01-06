#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL and displays the
body of the response.
prints the errorcode insteade where an error occurss
'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.post(url)
    code = req.status_code

    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
