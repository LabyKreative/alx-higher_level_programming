#!/usr/bin/python3
"""a script that takes in a URL, sends a request to same and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            response_content = str(response.read().decode('utf-8'))
            print(response_content)
    except urllib.error.HTTPError as error:
            print("Error code: {}".format(error.code))
