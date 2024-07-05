#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
And displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url, timeout=None)
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError as e:
        print("Error code:", response.status_code)
    except requests.RequestException as e:
        print("Error Code", response.status_code)
