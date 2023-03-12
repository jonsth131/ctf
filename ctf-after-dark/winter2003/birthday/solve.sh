#!/bin/bash

curl -s https://savannahalanis.github.io/birthday/ | grep 'flag{' | sed 's/.*\(flag{.*}\).*/\1/'
