from pycat.core import Window
from pycat.base import NumpyImage as Image

window = Window()
image = Image(255, 255)
for i in range(image.rows):
    for j in range(image.cols):
        image[i][j] = i

sprite = window.create_sprite()
sprite.texture = image.texture
sprite.position = window.center
window.run()

# Exercises
# 1. create a vertical gradient image (do not rotate sprite))
# 2. reverse the direction of the gradient
# 3. make every other row in the image black
# 4. create a gradient image for a 512 x 512 image
# 5. write a function to return a gradient image of arbitrary size
