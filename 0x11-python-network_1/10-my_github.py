#!/usr/bin/python3
"""
Displays the GitHub user id
Using Basic Authentication with a personal access token.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password), timeout=60)

    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)
