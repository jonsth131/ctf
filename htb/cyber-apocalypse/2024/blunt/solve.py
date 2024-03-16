#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from hashlib import sha256


def baby_step_giant_step(g, h, p):
    """Baby-step Giant-step algorithm for solving discrete logarithm problem."""
    m = int((p - 1) ** 0.5) + 1

    table = {pow(g, j, p): j for j in range(m)}

    giant_step = pow(g, -m, p)
    result = h
    for i in range(m):
        if result in table:
            return i * m + table[result]
        result = (result * giant_step) % p

    return None


if __name__ == "__main__":
    # Known parameters
    p = 0xDD6CC28D
    g = 0x83E21C05
    A = 0xCFABB6DD
    B = 0xC4A21BA9

    # Recover private keys
    a = baby_step_giant_step(g, A, p)
    b = baby_step_giant_step(g, B, p)

    if a is None or b is None:
        print("Failed to recover private keys")
        exit(1)

    print("Recovered private key a:", a)
    print("Recovered private key b:", b)

    # Compute shared secret using recovered private keys
    shared_secret = pow(A, b, p)
    assert shared_secret == pow(B, a, p)
    hash_value = sha256(long_to_bytes(shared_secret)).digest()[:16]

    # Provided ciphertext
    ciphertext = b"\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{"

    # Decrypt ciphertext using AES-CBC
    iv = b"\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*"
    cipher = AES.new(hash_value, AES.MODE_CBC, iv)

    # Decrypt ciphertext and remove padding
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print("Decrypted plaintext:", decrypted.decode())
