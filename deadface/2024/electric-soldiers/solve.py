#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Usage: solve.py <mp3>")
    sys.exit(1)

mp3 = sys.argv[1]

data = None
with open(mp3, "rb") as f:
    data = f.read()

if data is None:
    print("Failed to read file")
    sys.exit(1)

lsbs = []

for i in range(0, len(data)):
    lsbs.append(data[i] & 1)

lsbs = "".join([str(x) for x in lsbs])
chunks = [lsbs[i: i + 8] for i in range(0, len(lsbs), 8)]

secret = "".join([chr(int(x, 2)) for x in chunks])
secret = re.findall(r"flag{.*?}", secret)[0]

print(secret)
