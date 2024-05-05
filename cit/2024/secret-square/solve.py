#!/usr/bin/env python3
from PIL import Image

image = Image.open("secret_square.png")
flag = ""

for pixel in image.getdata():
    r, g, b = pixel
    flag += chr(r + g + b)

print(flag)
