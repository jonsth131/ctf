#!/usr/bin/env python3

from hashlib import pbkdf2_hmac
from base64 import b64decode
from Crypto.Cipher import AES

flag = b64decode(
    'mZzroGSIkpZlwvCwLG0PHQMXzjphDowlbeBayjWJhmYPJ5KiQeUAbcv9SzTnLGpr3uYQ0VvZ02rGlxz71tOXMemdK1DKKY6uX2QfUJW+WlDPcLi1u48xBrhmDcpRaK1G')
salt = b'DcRatByqwqdanchun'
masterkey = b64decode('S1hNZ2tQdFJlRkVIWXhKczRMZEIwRmRQVmg3WGxDNEQ=')

key = pbkdf2_hmac('sha1', masterkey, salt, 50000, 32)

print('key: ', key)

iv = flag[:16]
flag = flag[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
print('Decrypted:', cipher.decrypt(flag))
