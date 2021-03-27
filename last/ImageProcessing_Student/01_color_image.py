from pycat.core import Window
from pycat.base import NumpyImage as Image

window = Window()
image_rgb = Image(255, 255, 3)
for i in range(image_rgb.rows):
    for j in range(image_rgb.cols):
        if j < 85:
            image_rgb[i][j] = [255, 0, 0]
        elif j < 170:
            image_rgb[i][j] = [0, 255, 0]
        else:
            image_rgb[i][j] = [0, 0, 255]

sprite = window.create_sprite()
sprite.texture = image_rgb.texture
sprite.position = window.center
sprite.x -= sprite.width / 2

image_rgba = Image(255, 255, 4)
for i in range(image_rgba.rows):
    for j in range(image_rgba.cols):
        if j < 85:
            image_rgba[i][j] = [255, 0, 0, i]
        elif j < 170:
            image_rgba[i][j] = [0, 255, 0, i]
        else:
            image_rgba[i][j] = [0, 0, 255, i]

sprite = window.create_sprite()
sprite.texture = image_rgba.texture
sprite.position = window.center
sprite.x += sprite.width / 2

window.run()
