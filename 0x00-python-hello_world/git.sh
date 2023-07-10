#!/bin/bash

# Get the current date and time
now=$(date +"%Y-%m-%dT%H:%M:%S")

# Get a random commit message
commit_message="Automated commit ${now}"

# Git add all files
git add .

# Git commit with a random message
git commit -m "${commit_message}"

# Git push commits
git push

