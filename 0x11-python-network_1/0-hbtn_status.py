#!/usr/bin/python3
"""
This ia a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(body), body, body.decode('utf-8')))
