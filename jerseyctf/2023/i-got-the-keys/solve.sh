#!/bin/bash

curl -H "Authorization_key: GdERHpBh3x" https://jerseyctf-i-got-the-keys.chals.io/flag | grep -oE "jctf{.*}"
