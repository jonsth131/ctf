#!/usr/bin/env python3

import base64
from cryptography.fernet import Fernet

encMessage = b'gAAAAABj7Xd90ySo11DSFyX8t-9QIQvAPmU40mWQfpq856jFl1rpwvm1kyE1w23fyyAAd9riXt-JJA9v6BEcsq6LNroZTnjExjFur_tEp0OLJv0c_8BD3bg='
key_bytes = base64.b64decode(
    b'7PXy9PSZmf/r5pXB79LW1cj/7JT6ltPEmfjk8sHljfr6x/LyyfjymNXR5Z0=')

key = bytearray()

for k_b in key_bytes:
    key.append(k_b ^ 160)

fernet = Fernet(key)
decMessage = fernet.decrypt(encMessage).decode()

print(decMessage)
