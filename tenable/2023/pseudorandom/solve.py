#!/usr/bin/env python3

import time
import random
import base64
import pytz
from datetime import datetime
from Crypto.Cipher import AES


def get_key(timestamp):
    random.seed(timestamp)
    key = []
    for i in range(0, 16):
        key.append(random.randint(0, 255))
    return bytes(key)


def decrypt(enc, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc)


def get_timestamp():
    tz = pytz.timezone('US/Mountain')
    date = tz.localize(datetime(2023, 8, 2, 10, 27)).astimezone(
        pytz.utc).strftime('%Y-%m-%d %H:%M')
    timestamp = time.mktime(time.strptime(date, '%Y-%m-%d %H:%M'))
    return round(timestamp*1000)


if __name__ == '__main__':
    enc = base64.b64decode(
        b'lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y')
    iv = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
    timestamp = get_timestamp()

    for i in range(0, 100000):
        key = get_key(timestamp+i)
        try:
            decrypted = decrypt(enc, iv, key)
            if b'flag' in decrypted:
                print(decrypted.replace(b'\x00', b'').decode())
                break
        except:
            pass
