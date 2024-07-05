#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
Using requests module
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    resp = requests.get(url, timeout=None)

    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
