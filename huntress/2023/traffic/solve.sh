#!/bin/bash

URL="https://"$(zcat */ssl.* | cut -d$'\t' -f 10 | grep sketchy | uniq)

echo "Found url: $URL"

curl -s $URL | grep -oE "flag{.*}"
