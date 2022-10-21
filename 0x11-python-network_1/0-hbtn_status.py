#!/usr/bin/python3
"""This module fetches a url using urllib"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)).expandtabs(4))
    print("\t- content: {}".format(content).expandtabs(4))
    print("\t- utf8 content: {}".
          format(content.decode(response.headers.get_content_charset()))
          .expandtabs(4))
