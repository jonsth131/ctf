#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageChops

FONT_FILE = "LiberationMono-Regular.ttf"
FLAG_POSITION = (90, 280)

blurred_img = Image.open("card.png")

font = ImageFont.truetype(FONT_FILE, size=50)
small_font = ImageFont.truetype(FONT_FILE, size=14)

flag_prefix = 'cratectf{'
flag_suffix = '}'
cw = 30
ch = 42

found = ''

for part in range(8):
    for i in range(100):
        test_part = str(i).zfill(2)
        test = found + test_part + '11' * (7 - part)
        test = test[:4] + ' ' + test[4:8] + ' ' + test[8:12] + ' ' + test[12:]

        img = Image.open("card_blank.png")
        draw = ImageDraw.Draw(img)

        draw.text((5, FLAG_POSITION[1] + 18),
                  flag_prefix, font=small_font, fill=("white"))
        width, height = draw.textsize(test, font=font)
        draw.text((FLAG_POSITION[0] + width + 10, FLAG_POSITION[1] + 18),
                  flag_suffix, font=small_font, fill="white")

        # Print flag onto base image
        draw.text(FLAG_POSITION, test, font=font, fill="white")

        flag_coords = (FLAG_POSITION[0], FLAG_POSITION[1],
                       FLAG_POSITION[0] + width, FLAG_POSITION[1] + height)
        flag_part = blurred_img.crop(flag_coords)
        blur_part = img.crop(flag_coords)
        blur_part = blur_part.filter(ImageFilter.BoxBlur(radius=20))
        add = 0
        if part > 1:
            add += cw
        if part > 3:
            add += cw
        if part > 5:
            add += cw
        x = cw * (part * 2) + add
        char_coords = (x, 0, x+cw, ch)
        blur_part = blur_part.crop(char_coords)

        ch_part = flag_part.crop(char_coords)
        diff = ImageChops.difference(ch_part, blur_part)

        if not diff.getbbox():
            found += test_part
            break

flag = flag_prefix + found[:4] + ' ' + found[4:8] + ' ' + found[8:12] + ' ' + found[12:] + flag_suffix
print(flag)
