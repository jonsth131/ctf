#!/usr/bin/env python3


def get_key(enc):
    known_pt_len = 38
    with open("emails/email0.txt", "rb") as f:
        email = f.read()

    known_pt_start = email[:5]
    known_pt = email[len(email) - known_pt_len :]
    enc_known_pt = enc[len(enc) - known_pt_len :]

    key = bytes([known_pt[i] ^ enc_known_pt[i] for i in range(known_pt_len)])

    for i in range(2, len(key)):
        if key[i] == key[0] and key[i + 1] == key[1]:
            key = key[:i]
            break

    decoded_start = b""

    while decoded_start != known_pt_start:
        key = key[1:] + key[:1]
        decoded_start = bytes([enc[i] ^ key[i % len(key)] for i in range(5)])

    return key


if __name__ == "__main__":
    with open("emails/email5.enc", "rb") as f:
        enc = f.read()

    key = get_key(enc)

    decoded = bytes([enc[i] ^ key[i % len(key)] for i in range(len(enc))])

    print(decoded.decode())
