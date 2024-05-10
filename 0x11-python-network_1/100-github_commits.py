#!/usr/bin/python3
"""
Write a python script to solve the given challenge
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    R = requests.get(url)
    commits = R.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
