#!/usr/bin/env python3


def get_key(encrypted, crib):
    key = []
    for i in range(len(crib)):
        key.append(encrypted[i] ^ crib[i])
    return key


def decrypt(encrypted, key):
    decrypted = ''
    for i in range(len(encrypted)):
        decrypted += chr(encrypted[i] ^ key[i % len(key)])
    return decrypted


def main():
    flag = bytes.fromhex(
        '982a9290d6d4bf88957586bbdcda8681de33c796c691bb9fde1a83d582c886988375838aead0e8c7dc2bc3d7cd97a4')
    crib = b'uoftctf{'
    key = get_key(flag, crib)
    print(decrypt(flag, key))


if __name__ == '__main__':
    main()
