#!/usr/bin/python3
"""
Write a python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
from sys import argv

if __name__ == '__main__':
    Qu = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    R = requests.post(url, data={'q': Qu})
    try:
        r_dict = R.json()
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
