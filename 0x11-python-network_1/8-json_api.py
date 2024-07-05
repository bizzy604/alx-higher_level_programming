#!/usr/bin/python3
"""
Takes in a letter and sends a POST request
To http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    try:
        data = {"q": sys.argv[1]}
    except IndexError:
        data = {"q": ""}

    try:
        response = requests.post(url, data=data, timeout=None)
        response_json = response.json()

        if response.json():
            Id = response.json()['id']
            name = response.json()['name']
            print(f"[{Id}] {name}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
