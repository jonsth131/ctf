target = b'WhatAreYouDoingToChallenge'
enc = b'\x3e\x06\x15\x1d\x26\x00\x0c\x2d\x06\x0e\x1d\x00\x1c\x31\x26\x26\x0a\x1c\x29\x0c\x0d\x16\x0c\x00\x00\x18'

def unknown_method(text_to_scramble, password):
    string_builder = []
    for i in range(len(text_to_scramble)):
        index = i % len(password)
        c = text_to_scramble[i]
        c = chr(c ^ password[index])
        string_builder.append(c)

    return ''.join(string_builder)


def main():
    flag = unknown_method(target, enc)
    print(flag)


if __name__ == '__main__':
    main()