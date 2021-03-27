from pycat.core import Window, Sprite, KeyCode
from pycat.base import NumpyImage as Image
# maybe skip this exercise
window = Window()
original_image = Image.get_array_from_file("baboon.jpeg")

# Exercise: implement the functions below
def get_max_rgb_image():
    rows, cols, channels = original_image.shape
    new_image = Image(rows, cols)
    for i in range(rows):
        for j in range(cols):
    # new_image[i][j] = max(r, g, b)
            new_image[i][j] = 255
            r, g, b, a = original_image[i][j]
            new_image[i][j] = max(r, g, b)
    return new_image


def get_luminance_image():
    rows, cols, channels = original_image.shape
    luminance_image = Image(rows, cols)
    for i in range(rows):
        for j in range(cols):
            r, g, b, a = original_image[i][j]
            luminance_image[i][j] = .299 * r + .587 * g + .114 * b
    return luminance_image


def get_complement_image():
    rows, cols, channels = original_image.shape
    complement_image = Image(rows, cols, channels)
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                r, g, b, a = original_image[i][j]
                complement_image[i][j] = [255-r, 255-g, 255-b, a]
    return complement_image


max_rgb_image = get_max_rgb_image()
luminance_image = get_luminance_image()
complement_image = get_complement_image()

# Extensions: add functions to extract the R G B functions


class ImageTest(Sprite):

    def on_create(self):
        self.texture = Image.get_texture_from_array(original_image)
        self.scale = 2
        self.position = window.center

    def on_update(self, dt):
        if window.get_key_down(KeyCode._1):
            self.texture = Image.get_texture_from_array(original_image)
        if window.get_key_down(KeyCode._2):
            self.texture = max_rgb_image.texture
        if window.get_key_down(KeyCode._3):
            self.texture = luminance_image.texture
        if window.get_key_down(KeyCode._4):
            self.texture = complement_image.texture


window.create_sprite(ImageTest)
window.run()
