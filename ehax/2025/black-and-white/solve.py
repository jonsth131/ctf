#!/usr/bin/env python3
from PIL import Image
import os


def create_image(data):
    img = Image.new('1', (len(data[0]), len(data)))

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '1':
                img.putpixel((j, i), 1)

    return img


files = os.listdir('out')

for file in files:
    data = open('out/' + file, 'r').read().strip().replace(' ', '')
    data = data.split('\n')
    img = create_image(data)
    img.save(f'img/{file}.png')
