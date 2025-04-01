#!/usr/bin/env python3

import hashlib
import string

alphabet = string.printable

"""
.data:0000000000842140 dword_842140 dd 0B0DE2CB4h, 4CEC9C5Fh, 0E91F6E53h, 0B0DE2CB4h, 949A9B62h, 0CA9BBAFAh
.data:0000000000842140                                         ; DATA XREF: real_main+91↑o
.data:0000000000842158 dd 6FB0CBA3h, 6FB0CBA3h, 6FB0CBA3h, 9688D99Fh, 0B319FFCEh, 0D3CF0FCCh
.data:0000000000842170 dd 4CEC9C5Fh, 6789B26h, 6789B26h, 0F7BAE229h, 17BE13CEh, 0B319FFCEh, 6FB0CBA3h
.data:000000000084218C dd 9688D99Fh, 0B319FFCEh, 4DFEC4CDh, 6789B26h, 0F7BAE229h, 0D58450Dh, 55FB6A31h
"""

table = [0x0B0DE2CB4, 0x4CEC9C5F, 0x0E91F6E53, 0x0B0DE2CB4, 0x949A9B62, 0x0CA9BBAFA, 0x6FB0CBA3, 0x6FB0CBA3, 0x6FB0CBA3, 0x9688D99F, 0x0B319FFCE, 0x0D3CF0FCC,
         0x4CEC9C5F, 0x6789B26, 0x6789B26, 0x0F7BAE229, 0x17BE13CE, 0x0B319FFCE, 0x6FB0CBA3, 0x9688D99F, 0x0B319FFCE, 0x4DFEC4CD, 0x6789B26, 0x0F7BAE229, 0x0D58450D, 0x55FB6A31]

"""
v6 |= v8[12] << 24;
  v6 |= v8[13] << 16;
  v6 |= v8[14] << 8;
  v6 |= v8[15];
"""


def hash(s):
    md5 = hashlib.md5(s)
    digest = md5.digest()
    v6 = 0
    v6 |= digest[12] << 24
    v6 |= digest[13] << 16
    v6 |= digest[14] << 8
    v6 |= digest[15]
    return v6


flag = ''

for v in table:
    for c in alphabet:
        h = hash(c.encode())
        if (h + v) & 0xFFFFFFFF == 0:
            print(f"Found: {c}")
            flag += c
            break

print(f"Flag: {flag}")
