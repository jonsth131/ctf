#!/usr/bin/env python3

encoded_flag = [
    578,
    568,
    248,
    588,
    573,
    573,
    508,
    543,
    618,
    258,
    553,
    533,
    243,
    608,
    478,
    608,
    243,
    588,
    573,
    478,
    533,
    263,
    593,
    263,
    478,
    498,
    243,
    513,
    513,
    258,
    258,
    478,
    273,
    258,
    288,
    253,
    278,
    263,
    628,
]

flag = ""

for c in encoded_flag:
    flag += chr((c - 3) // 5)

print(flag)
