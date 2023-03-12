#!/usr/bin/env python3

from scapy.all import *

a = rdpcap("EzPz.pcap")

data = b''

for packet in a:
    if b'0xL4' not in packet[TCP].load:
        val = packet[TCP].load[2:]
        if len(val) == 1:
            val = b'0' + val
        data += bytes.fromhex(val.decode())

open('out.png', 'wb').write(data)
