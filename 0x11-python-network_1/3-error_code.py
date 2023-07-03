#!/usr/bin/python3
"""a script that takes in a URL, sends a request to same and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    requests = urllib.request.Request(url=url)

    try:
        with urllib.request.urlopen(requests) as response:
            response_body = response.read()
            print(response_body.decode("utf-8"))
    except urllib.error.HTTPError as error:
            print(f"Error code: {error.code}")
