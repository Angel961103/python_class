from pycat.base.base_sprite import RotationMode
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
        if self.touching_any_sprite():
            print("You Lose!")
            w.close()
        if self.x>1200:
            print("You Win!")
            w.close()
        self.move_forward(10)


player=w.create_sprite(Turn)


class Enemy(Sprite):
    def on_create(self):
        self.rotation_mode=RotationMode
        self.image="ork1.png"
        self.scale=0.5
        self.x=w.width
        self.y=w.height
    def on_update(self, dt):
        self.point_toward_sprite(player)
        self.move_forward(2)


w.create_sprite(Enemy)
for i in range(150,1000,400):
    s=w.create_sprite()
    s.image="beach.png"
    s.x=i
    s.y=i
w.run()
