#!/bin/bash
# Get response status code without piping
curl -Is -w "%{http_code}" "$1"
