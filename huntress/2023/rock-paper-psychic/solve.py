#!/usr/bin/env python3

def rc4_decrypt(ciphertext, key):
    """Decrypt ciphertext (bytes) with key (bytes) using RC4."""

    # Initialize S-box
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Decrypt
    i = j = 0
    plaintext = bytearray(len(ciphertext))
    for k, c in enumerate(ciphertext):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        plaintext[k] = c ^ S[(S[i] + S[j]) % 256]

    return plaintext


def main():
    ciphertext = bytes.fromhex(
        'D1E2A0D9FA89CABED207EDF4F55C688E04EBE20F077351BDAA1E110D5A74805C916AF12F054C')
    key = b'gnnhexnyjkwpaghynzfthadollhtrhballsdmhhnbjppewgjkhnlhspwjswqoxtgdykxrhwlabblekxj'

    plaintext = rc4_decrypt(ciphertext, key)
    print(plaintext.decode())


if __name__ == '__main__':
    main()
