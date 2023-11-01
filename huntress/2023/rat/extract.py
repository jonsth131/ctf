#!/usr/bin/env python3

import re
import sys
import gzip


def extract_data(data, regex):
    match = re.search(regex, data)
    if match:
        return match.group(1)
    else:
        return None


def decode(data, pw):
    return bytes([x ^ pw for x in data])


def save(data, filename):
    data = gzip.decompress(data)
    with open(filename, 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: extract.py <file>')
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        data = f.read()

    libArr = bytes.fromhex(extract_data(
        data, b'<libArr>(.*)</libArr>').decode())
    fileArr = bytes.fromhex(extract_data(
        data, b'<fileArr>(.*)</fileArr>').decode())
    pass1 = int(extract_data(data, b'<pass1>(.*)</pass1>').decode()) % 256
    pass2 = int(extract_data(data, b'<pass2>(.*)</pass2>').decode()) % 256

    libArr = decode(libArr, pass1)
    fileArr = decode(fileArr, pass2)

    save(libArr, 'libArr.dll')
    save(fileArr, 'fileArr.exe')
