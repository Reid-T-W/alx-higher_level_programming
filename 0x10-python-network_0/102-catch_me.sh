#!/bin/bash
# Get custom response body usign curl
curl -so /dev/null -w "You got me!" "0.0.0.0:5000/catch_me"
