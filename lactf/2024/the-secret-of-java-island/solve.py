#!/usr/bin/env python3

from itertools import product
from hashlib import sha256

values = ['d', 'p']

for comb in product(values, repeat=8):
    hash = sha256(''.join(comb).encode()).digest()
    if hash.startswith(b'EF'):
        print('Found correct combination:', ''.join(comb))
