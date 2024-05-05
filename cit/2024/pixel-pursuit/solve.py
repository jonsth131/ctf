#!/usr/bin/env python3
import string


def get_fifth_bit(byte):
    return (byte >> 3) & 1


with open("image.jpeg.encoded", "rb") as f:
    data = f.read()

for i in range(0, len(data), 8):
    dec = get_fifth_bit(data[i]) << 7
    dec += get_fifth_bit(data[i + 1]) << 6
    dec += get_fifth_bit(data[i + 2]) << 5
    dec += get_fifth_bit(data[i + 3]) << 4
    dec += get_fifth_bit(data[i + 4]) << 3
    dec += get_fifth_bit(data[i + 5]) << 2
    dec += get_fifth_bit(data[i + 6]) << 1
    dec += get_fifth_bit(data[i + 7])
    decoded = chr(dec)
    if decoded in string.printable:
        print(decoded, end="")
        if decoded == "}":
            break
