#!/usr/bin/python3
'''
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API,
Print all commits by: `<sha>: <author name>` (one by line)
Write a Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
'''
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        }
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        commits = req.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print("{}: {}".format(sha, author))
    else:
        print("Error: {}".format(req.status_code))
