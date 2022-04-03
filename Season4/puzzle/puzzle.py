from pycat.core import Window
from pycat.base import NumpyImage

w = Window()
original_image = NumpyImage.get_array_from_file("view.PNG")
print(original_image.shape)

sub = original_image[:386, :567, :]
sub2 = original_image[386:, 567:, :]
# sub3 = original_image[386:, :567, :]
# sub4 = original_image[:386, 567:, :]

s = w.create_sprite(x=250,y=200)
s.texture = NumpyImage.get_texture_from_array(sub)
s2 = w.create_sprite(x=900,y=400)
s2.texture = NumpyImage.get_texture_from_array(sub2)
w.run()