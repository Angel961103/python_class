from pycat.window import Window
from pycat.sprite import Sprite
from random import randrange
window=Window()
class ClassSprite(Sprite):
    def on_create(self):
        self.image=("rooster.png")
        self.x=600
        self.y=300
        self.rotate(110)
        self.change_x(1)

for i in range(100):
    x=window.create_sprite(ClassSprite)

window.run()