#!/usr/bin/python3
"""Sends a post request urllib"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(req) as response:
        url = sys.argv[1]
        values = {'email': sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        content = response.read()
        print("{}".format(content.decode('utf-8')))
