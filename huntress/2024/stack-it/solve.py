#!/usr/bin/env python3

data1 = b"SQQUR^V\x07\x01\x04\x0d\x02\x00\x03V[\x0fP\x071SP\x0bPU\x00Q[\x01\x06S\x06"
data2 = b"1ecff8bece9486287dc76521a84bb7c0"

assert len(data1) == len(data2)
decoded = ""

for i in range(len(data1)):
    decoded += chr(data1[i] ^ data2[i])

print(f"flag{{{decoded}}}")
