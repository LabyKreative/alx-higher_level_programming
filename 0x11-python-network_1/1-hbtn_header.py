#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to same and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__=="main__":
    with urllbi.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
