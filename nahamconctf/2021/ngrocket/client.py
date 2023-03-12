#!/usr/bin/env python3

import time
from pwn import *

target = b'HOST:PORT'

while True:
    conn = remote('challenge.nahamcon.com', 0)

    conn.recv()
    conn.recv()
    conn.send(target)
    data = conn.recvuntil(b'ngrocket')
    print(data)

    conn.close()

    time.sleep(0.1)

    local = remote('localhost', 4444)

    local.send(data)
    local.close()
