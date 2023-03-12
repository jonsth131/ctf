#!/usr/bin/env python3

import socket
import json
import binascii

PLAINTEXT = b"A" * 64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("206.189.117.93", 31560))

s.recv(1024)
s.recv(1024)
s.sendall(b'{"option":"3"}') # Send command to change mode
s.recv(1024)
s.sendall(b'{"modes":["CTR"]}') # Send CTR as available mode
s.recv(1024)
s.recv(1024)
s.sendall(b'{"option":"2"}') # Send command to encrypt plaintext
s.recv(1024)
s.sendall(b'{"plaintext":"' + PLAINTEXT + b'"}') # Send plaintext to encrypt
encrypted_pt = json.loads(s.recv(1024).decode().strip())
s.recv(1024)
s.sendall(b'{"option":"1"}') # Get encrypted flag
encrypted_flag = json.loads(s.recv(1024).decode().strip())
s.close()

ct = binascii.unhexlify(encrypted_pt["ciphertext"])

# Recover key
key = bytearray()
for c in ct:
    key.append(c ^ ord("A"))

# Verify that key works with encrypted plaintext
pt = bytearray()
for i in range(0, len(ct)):
    pt.append(ct[i] ^ key[i % len(key)])

assert(all(x == 'A' for x in pt.decode()))

flag_ct = binascii.unhexlify(encrypted_flag["ciphertext"])

# Decrypt flag
flag = bytearray()
for i in range(0, len(flag_ct)):
    flag.append(flag_ct[i] ^ key[i % len(key)])

print('Flag:', flag)