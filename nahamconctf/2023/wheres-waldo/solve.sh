#!/bin/bash

curl -s http://challenge.nahamcon.com:30001/location\?lat\=40.5\&long\=-74.7 | grep -oE "flag{[0-9a-fn]{33}}"
