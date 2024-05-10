#!/usr/bin/python3
"""This script fetches data from
    https://alx-intranet.hbtn.io/status
"""


from urllib import request
url = "https://alx-intranet.hbtn.io/status"
with request.urlopen(url) as res:
    data = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode("utf-8")))
