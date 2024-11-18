#!/usr/bin/env python3
from Crypto.Cipher import AES


def decrypt_image_from_file(win_image_path, key, iv):
    try:
        with open(win_image_path, 'rb') as f:
            buffer = f.read()
        aes = AES.new(key, AES.MODE_CBC, bytes(iv))
        decrypted = aes.decrypt(buffer)
        return decrypted
    except Exception as ex:
        print(f"Decryption failed: {ex}")
        return None


def set_iv():
    array = [
        9, 59, 202, 213, 13, 62, 108, 125, 224, 15,
        10, 159, 13, 51, 70, 1
    ]
    b = 66
    for i in range(len(array)):
        array[i] ^= b
    return array


def main():
    win_image_path = "win.enc"
    key = "win.key"
    iv = set_iv()
    key = open(key, 'rb').read()
    decrypted = decrypt_image_from_file(win_image_path, key, iv)
    if decrypted:
        with open("win.png", 'wb') as f:
            f.write(decrypted)
        print("Decrypted image saved as win.png")


if __name__ == "__main__":
    main()
