#!/usr/bin/env python3

p = 307163712384204009961137975465657319439

with open('output.txt', 'r') as f:
    ciphertext = eval(f.read())


def legendre_symbol(c):
    return pow(c, (p - 1) // 2, p) == 1


bin_str = ''
for value in ciphertext:
    if legendre_symbol(value):
        bin_str += '0'
    else:
        bin_str += '1'

flag = int(bin_str, 2)
print(bytes.fromhex(hex(flag)[2:]).decode())
