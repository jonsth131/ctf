#!/usr/bin/env python3

flag = b'__1h}kup1t37ldD3lfga1_0r5_tO{wEH7_'

ss = [
    [0x10, 0x18],
    [0x1f, 0x13],
    [0xf, 0x17],
    [0x1e, 0x12],
    [0x9, 0x14],
    [0x1c, 0x1d],
    [0x16, 0x1a],
    [0x11, 0x21],
    [0x15, 0x19],
    [0xd, 0x7],
    [0xb, 0x1],
    [0x4, 0x0],
    [0xc, 0x20],
    [0x6, 0x2],
    [0x3, 0x1b],
    [0x8, 0xe],
    [0x5, 0xa],
]

temp = bytearray(len(flag))

for i in range(len(ss)):
    s = ss[i]
    temp[s[0]] = flag[s[1]]
    temp[s[1]] = flag[s[0]]

print(temp.decode()[::-1])