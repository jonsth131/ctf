#!/usr/bin/env python3

import base64


def decrypt(s1, s2):
    return ''.join((lambda a: [chr(ord(c1) ^ ord(c2)) for c1, c2 in a])(zip(s1, s2)))


def deobfuscate():
    part1 = '2ec7627d{galf'[::-1]
    part2 = str(base64.b64decode('NjIwM2I1Y2M2OWY0'.encode('ascii')), 'UTF8')
    part3 = decrypt('\x17*\x07`BC\x14*R@\x14^*', 'uKeVuzwIexplW')
    key = part1 + part2 + part3
    return key


print(deobfuscate())
