#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: solve.py [input file]")
    sys.exit(1)

data = None
with open(sys.argv[1], 'rb') as f:
    data = f.read()

decoded = bytearray()
for i in range(0, len(data), 3):
    val = data[i] + 0x50 & 0xff
    times = data[i + 1] << 8 | data[i + 2]
    print(val, times)
    decoded.extend([val] * times)

with open('decoded', 'wb') as f:
    f.write(decoded)

print("Decoded data written to 'decoded'")
