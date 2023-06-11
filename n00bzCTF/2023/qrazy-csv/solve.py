#!/usr/bin/env python3
import PIL.Image

f = open('secret.csv', 'r')
data = f.read()
f.close()

data = data.replace('"', '').split('\n')[1:]
data = [x.split(',') for x in data]

pixel_size = 10
img_size = 29 * pixel_size

img = PIL.Image.new('1', (img_size, img_size), color=1)

for p in data[:-1]:
    x = int(p[0])
    y = int(p[1])
    for i in range(pixel_size):
        for j in range(pixel_size):
            img.putpixel((x * pixel_size + i, y * pixel_size + j), 0)

img.save('flag.png')
