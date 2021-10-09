from pycat.window import Window
from pycat.sprite import Sprite
import random
from pycat.keyboard import KeyCode
window=Window()


class Owl(Sprite):
    def on_create(self):
        self.image="owl.gif"
        self.x=10
        self.y=450
    def on_update(self, dt):
        if window.get_key_down(KeyCode.O):
            self.change_x(random.randrange(0,100))
            self.scale=self.scale+0.1
        elif window.get_key(KeyCode.ENTER):
            self.scale=self.scale-0.01
        if self.scale==2():
            self.change_x(0)
        if self.touching_window_edge():
            print("owl win!")
            window.exit()
class Rooster(Sprite):
    def on_create(self):
        self.image="rooster.png"
        self.x=10
        self.y=150
    def on_update(self, dt):
        if window.get_key_down(KeyCode.R):
            self.change_x(random.randrange(0,100))
            self.scale=self.scale+0.1
        elif window.get_key(KeyCode.SPACE):
            self.scale=self.scale-0.01
        if self.touching_window_edge():
            print("rooster win!")
            window.exit()
        

window.create_sprite(Owl)
window.create_sprite(Rooster)
window.run()
