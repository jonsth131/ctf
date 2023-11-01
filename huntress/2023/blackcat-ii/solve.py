#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import hmac
import sys
import os
import hashlib


def get_files():
    return [
        'victim-files/Cafe_Terrace_at_Night_by_Vincent_van_Gogh_large.jpg.encry',
        'victim-files/flag.txt.encry'
    ]


def aes_decrypt_file(input_file, output_file, key):
    iv = bytes([1, 35, 69, 103, 137, 171, 205, 239, 254, 220,
                186, 152, 118, 84, 50, 16])
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        cipher = AES.new(key, AES.MODE_CFB, iv)
        while True:
            chunk = infile.read(4096)
            if not chunk:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            outfile.write(decrypted_chunk)


def generate_aes_key_from_password(password):
    salt = b'KnownSaltValue'
    return PBKDF2(password, salt, dkLen=32, count=10000,
                  prf=lambda p, s: hmac.new(p, s, hashlib.sha256).digest())


def calculate_sha256_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 solve.py <file-as-key>')
        return

    key = calculate_sha256_hash(sys.argv[1])
    print('Using initial key:', key)

    for filename in get_files():
        print('Decrypting', filename)
        outfile = os.path.join(os.path.splitext(filename)[0] + ".decry")
        aes_decrypt_file(filename, outfile,
                         generate_aes_key_from_password(key))
        key = calculate_sha256_hash(outfile)


def print_flag():
    print('-' * 80)
    with open('victim-files/flag.txt.decry', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    main()
    print_flag()
