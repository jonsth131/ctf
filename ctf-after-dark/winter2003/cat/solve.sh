#!/bin/bash

curl -s  https://savannahalanis.github.io/cat/vet.html | grep 'flag{' | sed 's/.*\(flag{.*}\).*/\1/'
