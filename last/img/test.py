from pycat.window import Window
from pycat.keyboard import KeyCode
from pycat.sprite import Sprite
w = Window(background_image="sea.png")
class Turn(Sprite):
    def on_create(self):
        self.image="owl.png"

    def on_update(self, dt):
        if w.get_key_down(KeyCode.W):
            self.rotation=90
        if w.get_key_down(KeyCode.A):
            self.rotation=180
        if w.get_key_down(KeyCode.S):
            self.rotation=270
        if w.get_key_down(KeyCode.D):
            self.rotation=0
        self.move_forward(5)



w.create_sprite(Turn)

w.run()