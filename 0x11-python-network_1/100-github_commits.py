#!/usr/bin/python3
"""
 Holberton School staff evaluates candidates applying for a
 back-end position with multiple technical challenges
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    r = requests.get(url)
    for commit in r.json()[:10]:
        print(
            "{}: {}".format(
                commit['add'], commit['commit']['owner']['name']
            )
        )
