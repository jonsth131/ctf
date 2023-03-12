#!/usr/bin/env python3
from pwn import *
from hashpumpy import hashpump
import json

def forge(salt_length, original_data, original_signature):
    data_to_add = "\nSELECT * FROM materials;"
    print(salt_length, original_data, original_signature)

    result = hashpump(original_signature.decode(),
                      original_data.decode(),
                      data_to_add,
                      salt_length)

    return result[0], result[1].hex()

r = remote('178.62.123.156', 32630)

r.recvuntil(b'> ')
r.sendline(b'1')
data = r.recvline()
original_data = bytes.fromhex(data[12:178].decode())
original_signature = data[195:-3]

i = 8

while True:
    print('Trying Salt length', i)
    r.recvuntil(b'> ')
    r.sendline(b'2')
    r.recvuntil(b'> ')
    (signature, data) = forge(i, original_data, original_signature)
    payload = json.dumps({'script': data, 'signature': signature})
    print(payload)
    r.sendline(payload.encode())
    resp = r.recvline()
    print('resp', resp)
    if b'Are you sure mister Frost signed this?' in resp:
        i += 1
    else:
        print(resp)
        break

print('Salt length', i)

r.interactive()
r.close()
