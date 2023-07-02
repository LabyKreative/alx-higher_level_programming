#!/bin/bash
# a script that takes in and send requests to a URL, using curl to retrieve number of bytes
curl -s "$1" | wc -c
