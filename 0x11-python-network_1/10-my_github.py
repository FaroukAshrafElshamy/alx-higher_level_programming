#!/usr/bin/python3

"""
Write a script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    request = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(request.json().get('id'))
