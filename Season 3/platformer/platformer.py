from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite

w = Window()
DV = 2
MAX_V = 20
FRCITION = 0.88
JUMP_SPEED = 25
GRAVITY = 1

class Platform(Sprite):
    def on_create(self):
        self.color = Color.AZURE
        self.add_tag("platform")
        self.height = 50
        self.width = w.width/6

class Player(Sprite):
    def on_create(self):
        self.scale = 60
        self.color = Color.AMBER
        self.y = 100
        self.x = 100
        self.vx = 0
        self.vy = 0
        self.is_on_platform = False

    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.D):
            self.vx += DV
            if self.vx > MAX_V:
                self.vx = MAX_V
        if w.is_key_pressed(KeyCode.A):
            self.vx -= DV
            if self.vx < -MAX_V:
                self.vx = -MAX_V
        if w.is_key_down(KeyCode.W) and self.is_on_platform:
            self.vy = JUMP_SPEED
            self.is_on_platform = False

        self.vy -= GRAVITY
        self.vx *= FRCITION

        prev_y = self.y
        self.x += self.vx
        self.y += self.vy

        platforms = w.get_sprites_with_tag("platform")
        for platform in platforms:
            top_y = platform.y + 0.5*(platform.height + self.height)
            bot_y = platform.y - 0.5*(platform.height + self.height)
            if prev_y >= top_y and self.is_touching_sprite(platform):
                self.vy = 0
                self.is_on_platform = True
                self.y = top_y
            elif prev_y < bot_y and self.is_touching_sprite(platform):
                self.vy = 0



w.create_sprite(Player)
ground = w.create_sprite(Platform, x=w.center.x, y=25)
ground.width = w.width
ground.height = 50


w.create_sprite(Platform, x=w.center.x, y=225)
w.create_sprite(Platform, x=w.center.x+200, y=300)

w.run()