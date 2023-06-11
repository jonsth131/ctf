#!/bin/bash

curl -s https://lness02.github.io/meangirls/flag.html | grep iodj | sed 's/.*\(iodj{.*}\).*/\1/' | tr '[d-za-c]' '[a-z]'
