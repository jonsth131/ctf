#!/usr/bin/env python3
"""
This script takes a filtered pcap, with only the ICMP-packets generated by the
exfiltration script, and decodes the data. The data is then written to a file
called Exfil.zip, which can be unzipped to get the flag in the docx file.
"""

import sys
from scapy.all import *


def xor(data, key):
    for i in range(len(data)):
        data[i] ^= key[i % len(key)]


if len(sys.argv) != 2:
    print("Usage: ./solve.py <pcap file>")
    sys.exit(1)

pcap = sys.argv[1]

a = rdpcap(pcap)

key = b'38e655ef-8-5-2023'

data = bytearray()
for p in a:
    data += p[Raw].load

print('Read {} bytes'.format(len(data)))

xor(data, key)

print('Decoded {} bytes'.format(len(data)))

print('Writing to Exfil.zip')
with open('Exfil.zip', 'wb') as f:
    f.write(data)
