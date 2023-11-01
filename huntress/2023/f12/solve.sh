#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

curl -s "$URL/capture_the_flag.html" | grep -oE "flag{.*}"
