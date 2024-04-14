#!/usr/bin/env python3
from scapy.all import *

pcap = rdpcap("space.pcapng")

flag = ""

for packet in pcap:
    if packet.haslayer(TCP):
        if packet[TCP].dport == 8008:
            flag += chr(packet.window)

print(flag)
