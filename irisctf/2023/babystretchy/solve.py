#!/usr/bin/env python3

from pwn import *

r = remote('stretchy.chal.irisc.tf', 10704)

data = r.recvuntil(b'Solution? ')
print(data)

solution = input('Solution? ')

r.send(solution.encode())

r.recvuntil(b'> ')

alphabet = '0123456789abcdef'

for c in alphabet:
    data = c * 64
    for c2 in alphabet:
        data2 = c2 * 64
        payload = data + data2
        print('Sending:', payload)
        r.sendline(payload.encode())

        resp = r.recv()
        if b'irisctf' in resp:
            print('Flag:', resp.decode())
            r.close()
            exit(0)

r.close()
