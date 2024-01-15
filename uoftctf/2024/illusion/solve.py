#!/usr/bin/env python3

import base64
import hashlib
from Crypto.Cipher import AES

key = hashlib.sha256('Tr3v0rC2R0x@nd1s@w350m3#TrevorForget'.encode('utf8')).digest()

data = 'C9XqWpYeqCIn8Dk8gCVtpdg47vm8e8peFqkfQJ6WVbUvL7ucvQ0ayWnKRBF2GI+ltFBWNMa+wawqeuvFK61RGvKVWogAqAVg4J7qmScn+HRF0QZFgEunXlAduM+16nnf'

decoded = base64.b64decode(data)

iv = decoded[:16]
ct = decoded[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)

pt = cipher.decrypt(ct)

print(pt)