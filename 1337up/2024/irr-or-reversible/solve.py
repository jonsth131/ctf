#!/usr/bin/env python3
from pwn import *

r = remote('irrorversible.ctf.intigriti.io', 1330)

payload = b'\x00' * 200

r.recvuntil(b'Please enter the text you would like to encrypt:\n')
r.sendline(payload)

data = r.recvuntil(b'Thank you for playing!')

print(data)
