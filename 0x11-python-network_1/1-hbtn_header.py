#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
value of the X-Request-Id variable
"""


from urllib import request
import sys

url = sys.argv[1]
Rec = request.Request(url)
with request.urlopen(Rec) as R:
    print(dict(R.headers).get('X-Request-Id'))
