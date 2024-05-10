#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""


import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    R = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(R.json().get('id'))
