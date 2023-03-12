#!/bin/bash

curl -s https://246012460124601.github.io/script.js | sed 's/.*\(flag{.*}\).*/\1/'
