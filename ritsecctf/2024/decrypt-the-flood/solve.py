#!/usr/bin/env python3
from scapy.all import *

pcap = rdpcap("evidence.pcap")

for packet in pcap:
    load = packet.load.decode()
    if "RS{" in load:
        print(f"{load}")
        break
