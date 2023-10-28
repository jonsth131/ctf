#!/usr/bin/python3
import sys
from scapy.all import rdpcap, IP
import re

if len(sys.argv) != 2:
    print("Usage: ./solve.py <pcap_file>")
    sys.exit(1)

pcap = rdpcap(sys.argv[1])

data = ""
for pkt in pcap:
    if IP in pkt and pkt[IP].src == "77.74.198.52":
        load = pkt.load.decode()
        for match in re.findall(r"[a-z0-9]{20,}", load):
            data += match

data = bytearray(bytes.fromhex(data))

for i in range(len(data)):
    data[i] ^= 0x1d

flag = re.search(r"HTB{.*}", data.decode())

print("Flag:", flag.group(0))
