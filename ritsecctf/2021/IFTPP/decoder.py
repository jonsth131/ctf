#!/usr/bin/env python3

from scapy.all import *
import hashlib
import base64
from urllib.parse import urlparse

"""
      SESSION_INIT = 0;     // client to propose session ID
      ACK = 1;              // generic ack, multiple uses
      CLIENT_KEY = 2;       // client proposed key
      SERVER_KEY = 3;       // server proposed key
      FILE_REQ = 4;         // client requesting file
      FILE_DATA = 5;        // requested file data
      FIN = 6;              // transfer is complete
      RETRANS = 7;           // request retrans of prev packet
"""
flags = {
   0: 'Session init',
   1: 'Ack',
   2: 'Client key',
   3: 'Server key',
   4: 'File request',
   5: 'File data',
   6: 'Fin',
   7: 'Retrans'
}

a=rdpcap("iftpp_challenge.pcap")

ckey = b''
skey = b''
filename = b''
filedata = b''
key = b''

def calc_key(key1, key2):
    combined = list(ckey + skey)
    combined.sort(reverse=True)
    combined = bytearray(combined)
    hash_object = hashlib.sha1(combined)
    return bytearray(base64.b64encode(hash_object.digest()))

def decrypt(data, key):
    decoded = bytearray()
    for idx in range(len(data)):
        decoded.append(data[idx] ^ key[idx % len(key)])
    return decoded

for packet in a[ICMP]:
    flag = packet.load[-1]
    if flag in flags:
        data_len = packet.load[3]
        data = packet.load[4:-12]
        checksum = packet.load[-10:-2]

        if flag == 2:
            ckey = data
        if flag == 3:
            skey = data
        if flag == 4:
            filename = data
        if flag == 5:
            data = packet.load[5:-12]
            key = calc_key(ckey, skey)
            decoded = decrypt(data, key)
            filedata += decoded
        
        print(flags[flag])

fh = open(filename, 'wb')
fh.write(filedata)
fh.close()