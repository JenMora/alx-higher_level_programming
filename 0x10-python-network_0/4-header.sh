#!/bin/bash
# takes in a URL as an argument, sends a GET request and displays
curl -s -H "X-School-User-Id: 98" "$1"
