#!/usr/bin/env python3

from pwn import *

r = remote("challenge.ctf.games", 31065)

for i in range(12):
    data = r.recvuntil(b"Your move: ")
    print(data.decode())
    if b"strike" in data:
        print("Block!")
        r.sendline(b"block")
    elif b"block" in data:
        print("Advance!")
        r.sendline(b"advance")
    elif b"advance" in data:
        print("Retreat!")
        r.sendline(b"retreat")
    elif b"retreat" in data:
        print("Strike!")
        r.sendline(b"strike")
    else:
        print("invalid data")
        break

data = r.recvall()
print(data.decode())
