#!/usr/bin/env python3

import string

target = [
    b"\xc2\xa8",
    b"\xc3\x88",
    b"\xc2\xa2",
    b"\xc3\x90",
    b"\xc2\xa8",
    b"\xc3\x89",
    b"\xc2\xaf",
    b"\xc3\x98",
    b"\xc3\x89",
    b"q",
    b"j",
    b"\xc2\xa0",
    b"\xc3\x87",
    b"\xc3\x8a",
    b"\xc2\xbf",
    b"j",
    b"J",
    b"\xc2\xa0",
    b"b",
    b"\xc3\x87",
    b"j",
    b"\xc2\xa0",
    b"P",
    b"q",
    b"H",
    b"\xc2\xa0",
    b"\xc2\xb8",
    b"H",
    b"\xc3\x92",
    b"\xc2\xa0",
    b"P",
    b"\xc2\x80",
    b"\xc2\xa0",
    b"\xc3\x89",
    b"\xc2\xb1",
    b"H",
    b"\xc2\xa0",
    b"p",
    b"A",
    b"\xc3\x81",
    b"\xc2\xb1",
    b"H",
    b"\xc3\x87",
    b"J",
    b"\xc2\xa0",
    b"\xc2\xba",
    b"b",
    b"R",
    b"B",
    b"h",
    b"\xc3\x9a",
]


def process_element(element):
    esi = element
    r8 = esi
    r9 = r8 + 0x17
    esi -= 1
    rsi = esi
    rsi = rsi << 1
    r9 = r9 ^ rsi
    rsi = r9
    r9_sign = (r9 >> 63) & 1
    r9 = r9_sign
    rsi = rsi + r9
    r9 = rsi & 0xFFFFFFFFFFFFFFFC
    rsi = rsi - r9
    rsi = rsi + r8 * 2
    rsi = rsi - 0x20

    return chr(rsi).encode()


flag = b""

for val in target:
    for c in range(256):
        try:
            res = process_element(c)
        except:
            continue
        if res == val:
            flag += chr(c).encode()
            break

print(flag.decode())
