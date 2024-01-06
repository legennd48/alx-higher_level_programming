#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to
the URL, and displays the value of the variable
X-Request-Id in the response header
'''
from sys import argv
import requests


url = argv[1]
req = requests.get(url)
x_id = req.headers.get('X-Request-Id')

print("{}".format(x_id))
