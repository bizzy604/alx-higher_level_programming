#!/usr/bin/python3
"""
Module for a script that takes in a URL,
sends a request to the URL
And displays the body of the response (decoded in utf-8).
"""
import sys
from urllib.error import HTTPError
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode('utf-8')
        print(content)
    except HTTPError as e:
        print("Error code:", e.code)
