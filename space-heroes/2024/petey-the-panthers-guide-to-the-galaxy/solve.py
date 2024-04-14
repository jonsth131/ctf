#!/usr/bin/env python3
import PIL.Image


# Combine images into one image, given a list of images
# Combine the images in to a square grid
def combine_images(images):
    width, height = images[0].size
    new_im = PIL.Image.new("RGB", (width * 20, height * 20))
    for i in range(400):
        x = i % 20
        y = i // 20
        new_im.paste(images[i], (x * width, y * height))
    return new_im


def read_images():
    images = []
    for i in range(400):
        print(f"Reading piece {i}")
        images.append(PIL.Image.open(f"secrets/piece_{i}.png"))
    return images


if __name__ == "__main__":
    images = read_images()
    new_im = combine_images(images)
    new_im.save("flag.png")
    new_im.show()
