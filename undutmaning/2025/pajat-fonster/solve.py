#!/usr/bin/env python3
import struct

data1 = [0xBBBA9C95, 0xD6F58B6E, 0x2C983590, 0x835F6552,
         0xBE1B02C4, 0xC92DC639, 0x614C9C92, 0x4D]
data2 = [0xCEDEF2E0, 0xE682F01A, 0x73A96AE7, 0xB029553E,
         0xCB77609B, 0xBB4EF30A, 0x5422AFA1, 0x30]

for i in range(8):
    data1[i] ^= data2[i]

flag = struct.pack("<8I", *data1)
print(flag)
