#!/usr/bin/env python3

flag = b'\323\341\356\347\365\351\356\345\302\362\357\364\350\345\362\200Stb3Unkn0wn'

for i in range(len(flag)):
    val = flag[i] ^ 0x80
    if val == 0:
        print()
        exit()
    print(chr(val), end='')
