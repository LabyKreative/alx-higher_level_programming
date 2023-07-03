#!/usr/bin/python3
"""a script that takes in a URL and an email address, sends a POST request to
same with the email as a parameter, and finally displays the body of the res.
"""
import sys
import requests


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    body = requests.post(sys.argv[1], data=email)
    print(body.text)
