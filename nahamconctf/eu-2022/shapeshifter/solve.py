#!/usr/bin/env python3

def decrypt(data):
    values = [int(c) for c in data.strip()]

    for _ in range(31337):
        newbit = values[0] ^ values[14] ^ values[13] ^ values[11]
        values = values[1:] + [newbit]

    return ''.join([str(c) for c in values])


data = open('output.txt', 'r').readlines()

binary_flag = ''.join([decrypt(line) for line in data])
flag = ''.join(chr(int(binary_flag[i*8:i*8+8], 2))
               for i in range(len(binary_flag)//8))

print(flag)
