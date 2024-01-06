#!/usr/bin/python3
'''
Script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
'''
from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    url = 'https://api.github.com/users/' + username
    token = argv[2]
    headers = {
        'Authorization': 'Bearer ' + token,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        userData = req.json()
        print(userData.get('id'))
    else:
        print('None')
