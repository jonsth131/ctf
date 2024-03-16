#!/usr/bin/env python3
import re
import base64


def decrypt(data):
    """
    Custom decryption algorithm found in the VBA script in the document
    """
    xor_key = 45
    for i in range(len(data)):
        data[i] = data[i] ^ xor_key
        xor_key = ((xor_key ^ 99) ^ (i % 254))
    return data


def rc4_decrypt(data, key):
    """
    RC4 decryption algorithm used in the first javascript payload
    """
    S = list(range(256))
    j = 0
    out = []
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])
    return bytes(out)


with open('invitation.docm', 'rb') as f:
    data = f.read()

# Extract and decrypt the encrypted data as in the VBA script in the document
idx = [m.end(0) for m in re.finditer(b'sWcDWp36x5oIe2hJGnRy1iC92AcdQgO8RLioVZWlhCKJXHRSqO450AiqLZyLFeXYilCtorg0p3RdaoPa', data)][0]
encypted = data[idx:idx+13082]
decrypted = decrypt(bytearray(encypted)).decode('utf-8')

# Extract and decrypt next payload from the decrypted javascript
# RC4 key found in the VBA script
s2 = re.findall(r'var r="(.*)"', decrypted)[0]
s2 = rc4_decrypt(base64.b64decode(s2), b'vF8rdgMHKBrvCoCp0ulm')

# Extract the flag from the second decrypted javascript payload
# Flag found as a request header, base64 encoded
flag = re.findall(r'flag=(.*)"', s2.decode('utf-8'))[0]
flag = base64.b64decode(flag).decode('utf-8')

print(flag)