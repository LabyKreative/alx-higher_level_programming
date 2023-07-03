#!/usr/bin/python
"""a script that takes in a URL, sends a request to same
and displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req_body = requests.get(url)
    if req_body.status_code >= 400:
        print("Error code: {}".format(req_body.status_code))
    else:
        print(req_body.text)
