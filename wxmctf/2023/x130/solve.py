#!/usr/bin/env python3
import struct

flag = bytearray(
    b'\x00\x01\xf5\xf6\x11\xf2\x15\xfe\xe8\r\xca\xfd*\x0e\x0c\xe6\x03\x03\x07\x03\x07\xef\xff\x19')

decoded = ''

calc_val = 0x77

for i in range(len(flag)):
    calc_val = struct.unpack('b', flag[i].to_bytes(
        1, byteorder='little'))[0] + calc_val
    decoded += chr(calc_val)

print(decoded)
