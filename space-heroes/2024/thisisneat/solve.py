#!/usr/bin/env python3
from Crypto.Cipher import AES

ct = bytes.fromhex(
    "2a21c725b4c3a33f151be9dc694cb1cfd06ef74a3eccbf28e506bf22e8346998952895b6b35c8faa68fac52ed796694f62840c51884666321004535834dd16b1"
)

key = b"3153153153153153"
iv = bytearray(16)

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
pt = cipher.decrypt(ct)
print(pt)
