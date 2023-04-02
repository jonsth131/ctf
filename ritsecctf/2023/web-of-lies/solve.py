#!/usr/bin/env python
import binascii
from scapy.all import *

r = rdpcap('weboflies.pcapng')

flag = '0b'

for packet in r:
    if Raw in packet:
        load = packet[Raw].load
        if b'/flag' in load:
            flag += '0'
        elif b'/fl4g' in load:
            flag += '1'

flag = int(flag, 2)
flag = binascii.unhexlify('%x' % flag)
print(flag.decode('utf-8'))
