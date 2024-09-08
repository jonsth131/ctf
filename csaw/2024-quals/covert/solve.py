#!/usr/bin/env python3
from scapy.all import *
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <pcap>")
    sys.exit(1)

pcap = rdpcap(sys.argv[1])

key = None
flag = ""

for pkt in pcap:
    if pkt.haslayer(IP) and pkt[IP].src == "172.20.10.5" and pkt[IP].dst == "172.57.57.57":
        data = pkt[IP].id
        if key is None:
            key = data // ord("c")
        flag += chr(data // key)

print(flag)
