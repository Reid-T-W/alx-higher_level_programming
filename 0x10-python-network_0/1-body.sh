#!/bin/bash
# Sends GET request and displays response body only if status code is 200
curl -s --fail "$1"
