#!/usr/bin/env python3
import base64
import re

evil_string = base64.b64decode(
    "cmpkdjNjYzE6MzUuU1R8aHY0dHR6YGd2b2R1MnBvfi46MTI0M3M6amcz"
)

decryptedChars = ""

for c in evil_string:
    decryptedChars += chr(c - 1)

flag = re.findall(r"RS{.*}", decryptedChars)[0]

print(flag)
