#!/usr/bin/env python3
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import os


def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    iv = encrypted[:16]
    encrypted = encrypted[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)

    return unpad(decrypted, 16)


def encrypt(data, key):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data.encode(), 16))

    return base64.b64encode(iv + encrypted).decode()


s = requests.Session()

base_url = "http://94.237.52.239:38540"

r = s.post(base_url + "/api/request-session-parameters")
r = r.json()

print(r)

g = int(r["g"], 16)
p = int(r["p"], 16)

print(f"g: {g}, p: {p}")

r = s.post(base_url + "/api/init-session", json={"client_public_key": 3})
r = r.json()

print(r)

server_pub_key = int(r["server_public_key"], 16)

print(server_pub_key)
session_key = sha256(str(server_pub_key).encode()).digest()

r = s.post(base_url + "/api/request-challenge")
r = r.json()

print(r)

encrypted_challenge = r["encrypted_challenge"]

print(encrypted_challenge)

challenge = sha256(decrypt(encrypted_challenge, session_key)).hexdigest()
packet_data = encrypt("flag", session_key)

r = s.post(
    base_url + "/api/dashboard",
    json={"challenge": challenge, "packet_data": packet_data},
)
r = r.json()

print(r)

print(decrypt(r["packet_data"], session_key))
