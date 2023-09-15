#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw

lines = sys.stdin.read().splitlines()

x = 800
y = 300

img = Image.new("RGB", (1200, 1000), color="white")
dr = ImageDraw.Draw(img)

for line in lines:
    split = line.split()
    if len(split) == 2:
        x += int(split[0])
        y += int(split[1])
        dr.point((x, y), fill="black")

img.show()
