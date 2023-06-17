#!/usr/bin/env python3
from Crypto.Cipher import AES

f = open('encrypted', 'rb')
data = f.read()
f.close()

alphabet = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

indices = [35, 33, 35, 10, 46, 20, 5, 30, 47, 43, 13, 24, 46, 24, 9,
           34, 8, 24, 28, 61, 54, 23, 55, 14, 5, 39, 38, 13, 27, 44, 59, 0]

key = bytearray()

for i in indices:
    key.append(alphabet[i])

salt = data[0:16]
data = data[16:]

aes = AES.new(key, AES.MODE_CBC, salt)

decrypted = aes.decrypt(data)

f = open('decrypted.jpg', 'wb')
f.write(decrypted)
f.close()

print('Flag in decrypted.jpg')
