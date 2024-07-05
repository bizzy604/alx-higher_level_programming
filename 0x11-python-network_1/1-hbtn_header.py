#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        headers = res.info()
    print(headers['X-Request-Id'])
