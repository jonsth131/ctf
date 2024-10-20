#!/usr/bin/env python3

from PIL import Image
import sys

if len(sys.argv) != 2:
    print("Usage: solve.py <csv>")
    sys.exit(1)

filename = sys.argv[1]
data = []
with open(filename, "r") as f:
    data = f.read().strip().split("\n")

for i in range(len(data)):
    data[i] = data[i].split(",")

zoom = 24

width = len(data[0])
height = len(data)

# create a new BW Image
img = Image.new("1", (width * zoom, height * zoom))

for x in range(width):
    for y in range(height):
        currx = x * zoom
        curry = y * zoom
        if data[y][x] == "255":
            for i in range(zoom):
                for j in range(zoom):
                    img.putpixel((currx + i, curry + j), 0)
        else:
            for i in range(zoom):
                for j in range(zoom):
                    img.putpixel((currx + i, curry + j), 1)

img = img.rotate(270)
img.save("flag.png")
