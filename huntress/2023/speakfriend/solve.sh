#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

curl $URL -A "Mozilla/5.0 93bed45b-7b70-4097-9279-98a4aef0353e" -kL
