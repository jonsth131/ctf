#!/usr/bin/env python3
import requests
import base64
from Crypto.Cipher import AES

url = 'https://gist.githubusercontent.com/HuskyHacks/8cece878fde615ef8770059d88211b2e/raw/abcaf5920a40843851eec550d1dca97e9444ac75/gistfile1.txt'

r = requests.get(url)

data = base64.b64decode(r.text)

key = b'rAcbUUWWNFlqMbruiYOIsAyVQHS78orv'
iv = b'MoJ8C6O4D3asAApB'

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(data)

print(decrypted)
