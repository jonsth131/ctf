#!/usr/bin/env python3
from scapy.all import *
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <pcap>")
    sys.exit(1)

pcap = rdpcap(sys.argv[1])

data = b''

for pkt in pcap:
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:
        data += pkt[ICMP].load[-1].to_bytes(1, 'big')

with open('flag.png', 'wb') as f:
    f.write(data)

print("Flag saved to flag.png")
