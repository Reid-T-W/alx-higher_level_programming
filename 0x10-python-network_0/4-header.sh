#!/bin/bash
# sends a custom header variable
curl -H "X-School-User-Id: 98" -X GET "$1"
