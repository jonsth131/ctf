#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = bytearray([238, 236, 133, 123, 132, 215, 41, 111, 93, 8, 227, 45, 179,
                 170, 235, 139, 150, 187, 160, 231, 187, 46, 155, 206, 207,
                 143, 107, 226, 131, 54, 202, 248])

data = open('SaveFile.sav', 'rb').read()

iv = data[:16]
save_data = data[16:-32]

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(save_data), AES.block_size)

print(pt.decode())
