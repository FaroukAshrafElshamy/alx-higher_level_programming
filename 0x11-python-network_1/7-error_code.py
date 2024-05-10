#!/usr/bin/python3
"""
Write a python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""


import requests
from sys import argv

if __name__ == '__main__':
    R = requests.get(argv[1])
    status = R.status_code
    print(R.text) if status < 400 else print(
        "Error code: {}".format(R.status_code))
