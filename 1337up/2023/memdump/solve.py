salt = b"lARqpBuxfjrYtxRvJ7x64AnueWSj8ypfSqTYnZkd"
VALUES = [37, 15, 6, 56, 55, 16, 60, 44, 47, 17, 71, 41, 71, 27, 99, 66, 38, 104, 10, 6, 87, 42, 91, 42]

salt2 = b"RheO5PB6mfL5N3YBH45e5XuCEaWpvWUFESqTYnZk"
VALUES2 = [0x20, 0x07, 0x06, 0x24, 0x46, 0x27, 0x2b, 0x42, 0x05, 0x05, 0x24, 0x54, 0x23, 0x43, 0x2a, 0x3f]

def magic(passparam, crypt):
    bytes = passparam
    crypt2 = bytearray(len(bytes))
    for i in range(len(bytes)):
        crypt2[i] = bytes[i] ^ crypt[i % len(crypt)]
    return crypt2

def main():
    code1 = magic(VALUES, salt)
    code2 = magic(VALUES2, salt2)

    print((code1 + code2).decode())

if __name__ == "__main__":
    main()