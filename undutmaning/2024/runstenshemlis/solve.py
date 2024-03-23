#!/usr/bin/env python3


def decrypt(randomInt, data):
    data = bytearray(data)
    for i in range(len(data)):
        data[i] ^= (randomInt + i) & 0xFF

    print(data.decode())


with open("secret.txt", "rb") as f:
    data = f.read()

decrypt(data[0], data[1:])
