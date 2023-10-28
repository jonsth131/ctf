#!/usr/bin/env python3

KEY = b'SUP3RS3CR3TK3Y'
CHECK = b'\xe9\xef\xc0V\x8d\x8a\x05\xbe\x8ek\xd9yX\x8b\x89\xd3\x8c\xfa\xdexu\xbe\xdf1\xde\xb6\\'


def reverse_transform(result):
    reversed_flag = []
    for i, value in enumerate(result):
        value += 74
        value &= 255
        value ^= KEY[i % len(KEY)]
        value -= 24
        value &= 255
        reversed_flag.append(value)
    return bytes(reversed_flag)


def main():
    transformed = reverse_transform(CHECK)
    print(transformed)


if __name__ == '__main__':
    main()