#!/usr/bin/python3
""" This is a sript that Fetches header from url passed as arg"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
