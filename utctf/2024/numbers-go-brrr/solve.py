#!/usr/bin/env python3

import time

from Crypto.Cipher import AES
from pwn import remote

orig_seed = (int(time.time() * 1000) % (10**6)) - 10_000


def get_key(seed):
    key = b""
    for _ in range(8):
        seed = int(str(seed * seed).zfill(12)[3:9])
        key += (seed % (2**16)).to_bytes(2, "big")
    return key


def decrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(message)
    return plaintext


r = remote("betta.utctf.live", 7356)

r.recvuntil(b"?\n")
r.sendline(b"1")
data = r.recvuntil(b"\n").strip()
r.close()

flag = bytes.fromhex(data.split(b": ")[1].decode())

for i in range(20_000):
    key = get_key(orig_seed + i)
    try:
        decrypted = decrypt(flag, key)
        if b"utflag" in decrypted:
            print("Flag:", decrypted, "Seed:", orig_seed + i)
            break
    except ValueError:
        continue
