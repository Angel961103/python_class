from pycat.core import Window, Sprite
from pycat.base import NumpyImage

window = Window()


class ImageSprite(Sprite):

    def on_create(self):
        self.image = "baboon.jpeg"
        self.scale = 2
        self.y = window.height / 2


input_sprite = window.create_sprite(ImageSprite)
input_sprite.x = (window.width - input_sprite.width) / 2
output_sprite = window.create_sprite(ImageSprite)
output_sprite.x = (window.width + output_sprite.width) / 2


image = NumpyImage.get_array_from_texture(input_sprite.texture)
rows, cols, channels = image.shape

img = NumpyImage(rows, cols)
for i in range(rows):
    for j in range(cols):
        intensity = (j * 255) // (cols - 1)
        img[i, j] = intensity



# for i in range(rows):
#     for j in range(cols):
#         channel_sum = 0
#         # print(image[i][j])
#         for k in range(channels - 1):
#             channel_sum = max(channel_sum, image[i][j][k])
#         image[i][j] = [channel_sum, channel_sum, channel_sum, 255]

# for i in range(rows):
#     for j in range(cols):
#         for k in range(channels - 1):
#             image[i][j][k] = 255 - image[i][j][k]

# output_sprite.texture = NumpyImage.get_texture_from_array(image)


output_sprite.texture = img.texture
window.run()
