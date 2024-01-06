#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status and tabulates response
'''
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        page = response.read()
        headers = response.info()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))
