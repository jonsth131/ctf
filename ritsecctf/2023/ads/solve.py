#!/usr/bin/env python3
from scapy.all import *
import binascii

packets = rdpcap("flag.pcapng")

flag = '0b'

for packet in packets:
    if packet[ICMP].type == 9:
        flag += '0'
    elif packet[ICMP].type == 10:
        flag += '1'

flag = int(flag, 2)
flag = binascii.unhexlify('%x' % flag)
print(flag.decode('utf-8'))
