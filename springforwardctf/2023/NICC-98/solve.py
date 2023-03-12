#!/usr/bin/env python3
import requests
import re
import base64

url = "https://nicc-nicc-98.chals.io/js/nicc98.js"
regex = r"console\.log\(\"(.*)\"\)"

r = requests.get(url)
encoded = re.findall(regex, r.text)[0]

print(base64.b64decode(encoded).decode("utf-8"))
