from pycat.core import Window, Sprite, KeyCode
from player_controller import PlayerController, Controller2D
w = Window()

class Player(Sprite):
    def on_create(self):
        self.scale = 100
        self.control = Controller2D(self, 10)
    def on_update(self, dt):
        self.control.update()

class Player2(Sprite):
    def on_create(self):
        self.scale = 100
        self.control = Controller2D(self,10,KeyCode.UP,KeyCode.DOWN,KeyCode.LEFT,KeyCode.RIGHT)
    def on_update(self, dt):
        self.control.update()

w.create_sprite(Player)
w.create_sprite(Player2)
w.run()