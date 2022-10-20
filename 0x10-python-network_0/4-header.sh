#!/bin/bash
# sends a custom header variable
curl -X GET "$1" -H "X-School-User-Id:98"
