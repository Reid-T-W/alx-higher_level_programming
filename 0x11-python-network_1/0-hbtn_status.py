#!/usr/bin/python3
"""This module fetches a url using urllib"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".
          format(content.decode(response.headers.get_content_charset())))
