#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long


def ROTL(a, b):
    return (((a) << (b)) | ((a % 2**32) >> (32 - (b)))) % 2**32


def qr(x, a, b, c, d):
    x[a] += x[b]
    x[d] ^= x[a]
    x[d] = ROTL(x[d], 16)
    x[c] += x[d]
    x[b] ^= x[c]
    x[b] = ROTL(x[b], 12)
    x[a] += x[b]
    x[d] ^= x[a]
    x[d] = ROTL(x[d], 8)
    x[c] += x[d]
    x[b] ^= x[c]
    x[b] = ROTL(x[b], 7)


ROUNDS = 20


def chacha_block(inp):
    x = list(inp)
    for i in range(0, ROUNDS, 2):
        qr(x, 0, 4, 8, 12)
        qr(x, 1, 5, 9, 13)
        qr(x, 2, 6, 10, 14)
        qr(x, 3, 7, 11, 15)

        qr(x, 0, 5, 10, 15)
        qr(x, 1, 6, 11, 12)
        qr(x, 2, 7, 8, 13)
        qr(x, 3, 4, 9, 14)

    return [(a+b) % 2**32 for a, b in zip(x, inp)]


def decrypt(data):
    global state, buffer

    output = []
    for b in data:
        if len(buffer) == 0:
            buffer = b"".join(long_to_bytes(x).rjust(4, b"\x00")
                              for x in state)
            state = chacha_block(state)
        output.append(b ^ buffer[0])
        buffer = buffer[1:]
    return bytes(output)


def chacha_init(input):
    state = [0 for _ in range(16)]
    for i in range(0, len(input), 4):
        state[i//4] = bytes_to_long(input[i:i+4])

    return state


p = remote('babycha.chal.irisc.tf', 10100)

p.recvuntil(b'> ')
p.sendline(b'1')
p.recvuntil(b'? ')
p.sendline(b'\00'*64)
encrypted = p.recvline().replace(b'\n', b'').decode()
print('Got encrypted data:', encrypted)
p.recvuntil(b'> ')
p.sendline(b'2')
encrypted_flag = p.recvline().replace(b'\n', b'').decode()
print('Got encrypted flag:', encrypted_flag)
p.close()

state = chacha_init(bytes.fromhex(encrypted))
buffer = b""

state = chacha_block(state)

print('Flag:', decrypt(bytes.fromhex(encrypted_flag)).decode())
