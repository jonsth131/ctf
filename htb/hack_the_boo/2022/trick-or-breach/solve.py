#!/usr/bin env python3

from scapy.all import *
from binascii import unhexlify
from zipfile import ZipFile
from io import BytesIO
import re

a=rdpcap("capture.pcap")

data = bytearray()

for packet in a:
    if packet[IP].src == "192.168.1.10" and packet.haslayer(DNSQR):
        query = packet[DNSQR].qname
        query = query.replace(b".pumpkincorp.com.", b"")
        data += bytearray(query)

file = ZipFile(BytesIO(unhexlify(data)))

files = {name: file.read(name) for name in file.namelist()}

for f in files:
    flag = re.findall(r'HTB{.*}', files[f].decode())
    if len(flag) != 0:
        print('Flag:', flag[0])
        exit(0)
