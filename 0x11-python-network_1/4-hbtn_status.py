#!/usr/bin/python3
"""
Write a script that fetches https://intranet.hbtn.io/status
"""


import requests
if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    R = requests.get(url)
    text = R.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
