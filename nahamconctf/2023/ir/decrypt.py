#!/usr/bin/env python3
from Crypto.Cipher import AES
from os import listdir

key = b'7h3_k3y_70_unl0ck_4ll_7h3_f1l35!'


def decrypt_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        iv = data[4:20]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(data[20:])


for filename in listdir('./files'):
    if filename.endswith('.enc'):
        file_data = decrypt_file('./files/' + filename)
        with open(filename[:-4], 'wb') as f:
            f.write(file_data)
