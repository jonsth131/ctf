#!/usr/bin/env python3
import base64

import requests

URL = "https://beep-boop.ctf.ritsec.club/"

r = requests.get(URL + "robots.txt")

data = r.text.split("\n")[3]
flag = base64.b64decode(data).decode("utf-8")

print(flag)
