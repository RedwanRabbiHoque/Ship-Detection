import numpy as np
import sys
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


def detect(model, path):
    image = Image.open(path)
    pix = image.load()

    n_spectrum = 3
    width = image.size[0]
    height = image.size[1]

    # creat vector
    picture_vector = []
    for chanel in range(n_spectrum):
        for y in range(height):
            for x in range(width):
                picture_vector.append(pix[x, y][chanel])

    picture_vector = np.array(picture_vector).astype(
        "uint8"
    )