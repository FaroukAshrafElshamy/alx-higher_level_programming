#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body_response = response.read()
        print("Body response:")
        print(f"\t- type: {type(body_response)}")
        print(f"\t- content: {body_response}")
        print(f"\t- utf8 content: {body_response.decode('utf-8')}")
