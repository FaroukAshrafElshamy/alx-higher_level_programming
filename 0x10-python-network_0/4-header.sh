#!/bin/bash
# a Bash script that takes in a URL as an argument.
curl -s "$1" -X GET -H "X-School-User-Id: 98"
