#!/usr/bin/python3
'''
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
from sys import argv


if __name__ == "__main__":
    letter = argv[1] if len(argv) == 2 else ''
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    req = requests.post(url, data=payload)
    try:
        val = req.json()
        if val:
            print("[{}] {}".format(val.get('id'), val.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
