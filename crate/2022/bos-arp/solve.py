#!/usr/bin env python3

from scapy.all import *

a = rdpcap("bosarp.pcap")

data = bytearray()

flag_data = ''
for packet in a:
    if packet.haslayer(ARP) and packet[ARP].psrc == '8.8.8.8':
        flag_data += packet[ARP].hwsrc.replace(':', '')

print('Flag:', bytes.fromhex(flag_data).decode()[3:])
