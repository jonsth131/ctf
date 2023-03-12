#!/usr/bin/env python3

from Crypto.Cipher import AES
from base64 import b64decode
import string

unpad = lambda s: s[:-ord(s[len(s) - 1:])]
alphabet = string.digits

enc_key = 'CiMwl2sIlzwtT4Mdm0dmmtOVV79W1dV1kIhWVWJqcYaSZu0ti0aVIkFD6Gim3Uhx'
enc_flag = 'OpFUeq8AsLskv9nSZ1FHYRGvM912ufXYUGI82aiOeX7eFvno9VANOIyH9VXkRkeJYDD74nTLWF22pGsu1G6B4tKGNnjGZ9di1QEIhyDDoxU='


def decrypt(key, encrypted_text):
    encrypted_text = b64decode(encrypted_text)
    cipher = AES.new(key, AES.MODE_CBC, b'1234567812345678')
    return unpad(cipher.decrypt(encrypted_text))


for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                pin = a + b + c + d
                key = pin + pin + pin + pin
                decrypted_key = decrypt(key.encode(), enc_key)
                try:
                    decrypted_content = decrypt(decrypted_key, enc_flag)
                    if b"{'username':" in decrypted_content:
                        print('Pin found:', pin)
                        print('Decrypted data:', decrypted_content)
                        exit(0)
                except:
                    continue
