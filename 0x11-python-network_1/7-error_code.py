#!/usr/bin/python
"""a script that takes in a URL, sends a request to same
and displays the body of the response."""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    req = requests.get(url)
    error_code = req.status_code

    if error_code >= 400:
        print(f'Error code: {error_code}')
    else:
        print(req.text)
