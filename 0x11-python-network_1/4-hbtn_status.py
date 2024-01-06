#!/usr/bin/python3
'''
script that fetches https://alx-intranet.hbtn.io/status
using requests package
'''
import requests

req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
