#!/usr/bin/python3
"""
sends a param via post request and
check if the response body is a valid
json
"""
import requests
import sys


if __name__ == "__main__":
    if (sys.argv[2] not None):
        param_data = {'q': sys.argv[2]}
    else:
        param_data = {'q': ''}
    res = request.get(sys.argv[1], params=param_data)
    print("{}".format(res.text))
