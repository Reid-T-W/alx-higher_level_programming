#!/usr/bin/python3
"""This module fetches a url using urllib"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')  \
                                as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)).expandtabs(4))
        print("\t- content: {}".format(content).expandtabs(4))
        print("\t- utf8 content: {}".
              format(content.decode('utf-8'))
              .expandtabs(4))
        print(response.headers)
