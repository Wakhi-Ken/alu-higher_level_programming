#!/usr/bin/python3
"""request and displays the response"""
from urllib import request
with request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
