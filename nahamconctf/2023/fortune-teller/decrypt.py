#!/usr/bin/env python3
from Crypto.Cipher import AES

f = open('fortune_teller/res/raw/encrypted', 'rb')
data = f.read()
f.close()

key = b'you win this ctf'
salt = data[0:16]
data = data[16:]

aes = AES.new(key, AES.MODE_CBC, salt)

decrypted = aes.decrypt(data)

f = open('decrypted.jpg', 'wb')
f.write(decrypted)
f.close()
