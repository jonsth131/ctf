#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

ACCESS_CODE=$(curl -s -X POST $URL/back/the/hawks/invite/code | jq -r '.message' | tr '[a-zA-Z]' '[d-za-cD-ZA-C]')

echo "Access code: $ACCESS_CODE"

curl -s -L $URL/register --data "access_code=$ACCESS_CODE" | grep -oE "flag{.*}"
