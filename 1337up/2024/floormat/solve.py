#!/usr/bin/env python3

from pwn import *
import re

EXE = ELF("./floormat_sale")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("floormatsale.ctf.intigriti.io", 1339)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

payload = b"A" * 24

r.recvuntil(b"Enter your choice:")
# r.sendline(payload)

log.info(f"Sending payload")

r.interactive()

data = r.recvuntil(b"}")
data = re.findall(b"INTIGRITI{.*}", data)[0]

log.success(f"Flag: {data.decode()}")
