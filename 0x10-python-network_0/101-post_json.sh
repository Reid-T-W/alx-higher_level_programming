#!/bin/bash
# Send json post request
curl -sX POST "$1" -H 'Content-Type: Application/json' -d "$2" 
