#!/bin/bash
# a script that takes in a URL, sends a request to that URL,
# Use curl to retrieve the HTTP response header and pipe it
# to wc to count the number of bytes
curl -s "$1" | wc -c
