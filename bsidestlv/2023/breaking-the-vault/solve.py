#!/usr/bin/env python3

flag = b'\x03\x12(%$2\x15\x0d\x17sqsr:\x13\x04\x1e\x00\x11\x0a\x1e\x08\x12\x1e\x07\x14\x0f<'

decoded = [c ^ 0x41 for c in flag]

print(bytes(decoded).decode('utf-8'))
