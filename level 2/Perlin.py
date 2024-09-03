from PIL import Image
import numpy as np
from noise import pnoise2

width, height = 800, 600
scale = 100.0

image = Image.new("RGB", (width, height))
pixels = image.load()

for i in range(width):
    for j in range(height):
        n = pnoise2(i/scale, j/scale, octaves=6, persistence=0.5, lacunarity=2.0)
        value = int((n + 0.5) * 255)
        pixels[i, j] = (value, value, value)

image.show()
