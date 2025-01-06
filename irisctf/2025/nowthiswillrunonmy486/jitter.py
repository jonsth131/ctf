#!/usr/bin/env python3
import sys


def sub_59C5BF569249(a1, a2):
    return a2 & 7 | (8 * a1) & 0x38 | 0xFFFFFFC0


def read_dword(data, idx):
    return data[idx] | (data[idx + 1] << 8) | (data[idx + 2] << 16) | (data[idx + 3] << 24)


def write_dword(data, idx, value):
    data[idx] = value & 0xff
    data[idx + 1] = (value >> 8) & 0xff
    data[idx + 2] = (value >> 16) & 0xff
    data[idx + 3] = (value >> 24) & 0xff


def write_word(data, idx, value):
    data[idx] = value & 0xff
    data[idx + 1] = (value >> 8) & 0xff


def jit_op(data, idx):
    """
    JIT the current opcode at the given index
    """
    v4 = data[idx]
    match v4:
        case 0x17:
            v7 = read_dword(data, idx + 3)
            data[idx] = data[idx + 1] & 7 | 0xB8
            write_dword(data, idx + 1, v7)
            data[idx + 5] = 0x90
            data[idx + 6] = 0x90
            data[idx + 7] = 0x90
        case 0xC4:
            v9 = data[idx + 1]
            v10 = data[idx + 2]
            data[idx] = 0x42
            data[idx + 1] = 0x8B
            data[idx + 2] = (8 * v9) & 0x38 | 4
            data[idx + 3] = v10 & 7
            write_dword(data, idx + 4, 0x90909090)
        case 0xC5:
            v11 = data[idx + 1]
            v12 = data[idx + 2]
            data[idx] = 66
            data[idx + 1] = 0x89
            data[idx + 2] = (8 * v11) & 0x38 | 4
            data[idx + 3] = v12 & 7
            write_dword(data, idx + 4, 0x90909090)
        case 0xD6:
            v14 = data[idx + 1]
            v15 = data[idx + 2]
            write_word(data, idx, 0x8D4A)
            data[idx + 2] = (8 * v14) & 0x38 | 4
            data[idx + 3] = v15 & 7
            write_dword(data, idx + 4, 0x90909090)
        case 0xEA:
            write_dword(data, idx, 0x9090050F)
            write_dword(data, idx + 4, 0x90909090)
        case 0xE:
            data[idx] = 0x31
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 1], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0x90909090)
            write_word(data, idx + 6, 0x9090)
        case 0x6:
            data[idx] = 0x31
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 2], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0x90909090)
            write_word(data, idx + 6, 0x9090)
        case 0x60:
            data[idx] = 0x21
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 2], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0x90909090)
            write_word(data, idx + 6, 0x9090)
        case 0x1E:
            data[idx] = 0x39
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 2], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0xFC0950F)
            write_word(data, idx + 6, 0xC0B6)
        case 0x9A:
            v5 = 8 * read_dword(data, idx + 3) - (idx + 8)
            data[idx] = 0x85
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 1], data[idx + 1]) & 0xff
            write_word(data, idx + 2, 0x840F)
            write_dword(data, idx + 4, v5)
        case 0x7:
            data[idx] = 0x29
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 2], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0x90909090)
            write_word(data, idx + 6, 0x9090)
        case 0x82:
            v8 = 8 * read_dword(data, idx + 3) - (idx + 5)
            data[idx] = 0xE9
            write_dword(data, idx + 1, v8)
            data[idx + 5] = 0x90
            write_word(data, idx + 6, 0x9090)
        case 0xD5:
            write_dword(data, idx, 0x909090C3)
            write_dword(data, idx + 4, 0x90909090)
        case 0x62:
            data[idx] = 0x31
            data[idx +
                 1] = sub_59C5BF569249(data[idx + 2], data[idx + 1]) & 0xff
            write_dword(data, idx + 2, 0x90909090)
            write_word(data, idx + 6, 0x9090)
        case _:
            print(f"Unknown op {hex(v4)}, idx: {idx}")
            exit(-1)


def jitter(data):
    for i in range(0, len(data), 8):
        jit_op(data, i)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <main>")
        sys.exit(1)

    file = sys.argv[1]

    with open(file, "rb") as f:
        data = f.read()

    code_len = 888
    code_offset = 0x2218

    data = bytearray(data[code_offset:code_offset + code_len])
    jitter(data)

    with open("jitted.bin", "wb") as f:
        f.write(data)

    print("Jitted code written to jitted.bin")


if __name__ == "__main__":
    main()
