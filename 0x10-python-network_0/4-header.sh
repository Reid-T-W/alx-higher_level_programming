#!/bin/bash
# sends a custom header variable
curl -X GET -H "X-School-User-Id: 98" "$1"
