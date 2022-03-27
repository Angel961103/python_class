from pycat.core import Window, Sprite, KeyCode

class PlayerController:
    def __init__(self,
                 player:Sprite,
                 speed:float,
                 left:KeyCode=KeyCode.A,
                 right:KeyCode=KeyCode.D
                 ):
        self.left = left
        self.right = right
        self.speed = speed
        self.window:Window = player.window
        self.player = player
    def update(self):
        if self.window.is_key_pressed(keycode=self.left):
            self.player.x -= self.speed
        if self.window.is_key_pressed(keycode=self.right):
            self.player.x += self.speed


class Controller2D:
    def __init__(self,
                 player:Sprite,
                 speed:float,
                 up:KeyCode=KeyCode.W,
                 down:KeyCode=KeyCode.S,
                 left:KeyCode=KeyCode.A,
                 right:KeyCode=KeyCode.D
                 ):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.speed = speed
        self.window:Window = player.window
        self.player = player

    def update(self):
        if self.window.is_key_pressed(keycode=self.left):
            self.player.x -= self.speed
        if self.window.is_key_pressed(keycode=self.right):
            self.player.x += self.speed
        if self.window.is_key_pressed(keycode=self.down):
            self.player.y -= self.speed
        if self.window.is_key_pressed(keycode=self.up):
            self.player.y += self.speed