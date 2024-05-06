#!/usr/bin/env python3


def xor_data(start, key, data):
    for i in range(start, 0x3000 + 1):
        data[i] ^= key


def nop_data(start, data):
    for i in range(start, start + 25):
        data[i] = 0x90


def find_lea(start, data):
    for i in range(start, 0x3000):
        if (
            data[i] == 0x48
            and data[i + 1] == 0x8D
            and data[i + 2] == 0x0D
            and data[i + 4] == 0x00
            and data[i + 5] == 0x00
            and data[i + 6] == 0x00
        ):
            return (i, data[i + 3])
    return (None, None)


def find_xor(start, data):
    for i in range(start, 0x3000):
        if data[i] == 0x80 and data[i + 1] == 0xF3:
            return data[i + 2]
    return None


def find_xor_al(start, data):
    for i in range(start, 0x3000):
        if data[i] == 0x34:
            return data[i + 1]
    return None


def find_cmp(start, data):
    for i in range(start, 0x3000):
        if data[i] == 0x3C:
            return (i, data[i + 1])
    return (None, None)


data = bytearray(open("bin_fun", "rb").read())
start = 0x1222

while True:
    lea_idx, lea_len = find_lea(start, data)

    if lea_idx is None or lea_len is None:
        break

    start = lea_idx
    xor_val = find_xor(start, data)

    if xor_val is None:
        break

    print(f"LEA: {hex(lea_idx)}, {hex(lea_len)}")
    print(f"XOR: {hex(xor_val)}")

    start += lea_len
    xor_data(start, xor_val, data)
    nop_data(lea_idx, data)

start = 0x1222
flag = ""

while True:
    xor_val = find_xor_al(start, data)

    if xor_val is None:
        break

    print(f"XOR AL: {hex(xor_val)}")

    start += 2

    (idx, cmp_val) = find_cmp(start, data)

    if cmp_val is None or idx is None:
        break

    start = idx + 2

    print(f"CMP: {hex(cmp_val)}")

    flag += chr(cmp_val ^ xor_val)

print(flag)
