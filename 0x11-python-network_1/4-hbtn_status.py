#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    req_body = req.text
    print("Body response:\n"
          "\t- type: {}\n"
          "\t- content: {}".format(type(req_body), req_body))
