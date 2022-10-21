#!/usr/bin/python3
"""This module fetches a url using urllib"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')  \
                                as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".
              format(content.decode('utf-8')))
        print(response.headers)
