#!/usr/bin/env python3
from scapy.all import *
from PIL import Image
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <pcap>")
    sys.exit(1)

pcap = rdpcap(sys.argv[1])

data = []
for pkt in pcap:
    if pkt["TCP"]:
        if len(pkt["TCP"].payload) == 32:
            data.append(pkt["TCP"].payload.load.decode())

zoom = 16

width = len(data[0])
height = len(data)

# create a new BW Image
img = Image.new("1", (width * zoom, height * zoom))

for x in range(width):
    for y in range(height):
        currx = x * zoom
        curry = y * zoom
        if data[y][x] == "Q":
            for i in range(zoom):
                for j in range(zoom):
                    img.putpixel((currx + i, curry + j), 0)
        else:
            for i in range(zoom):
                for j in range(zoom):
                    img.putpixel((currx + i, curry + j), 1)

img.save("flag.png")
