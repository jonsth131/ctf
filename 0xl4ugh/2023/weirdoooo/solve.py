#!/usr/bin/env python3

from PIL import Image

data = open('Weirdoooo.txt', 'r').readlines()

size = len(data[0].split(' '))-1, len(data)

print(size)

image = Image.new('L', size, 0)

for i in range(1024):
    row = data[i].split(' ')
    for j in range(1024):
        image.putpixel((i, j), int(row[j]))

image.show()
