#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

wget -m --http-user=opendir --http-password=opendir $URL
grep -r "flag{.*}" *
