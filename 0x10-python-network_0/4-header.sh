#!/bin/bash
# sends a custom header variable
curl -H "X-School-User-Id: 98" "$1"
