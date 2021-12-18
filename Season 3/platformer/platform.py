from pycat.base.base_sprite import RotationMode
from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite


DV = 2
MAX_V = 15
FRCITION = 0.78
JUMP_SPEED = 17
GRAVITY = 1

class Platform(Sprite):
    def on_create(self):
        self.color = Color.AZURE
        self.add_tag("platform")
        self.height = 50
        self.width = 200

        
        
class MovingPlatform(Platform):
    def on_create(self):
        self.state = 0
        self.add_tag("keyplatform")
        super().on_create()

    def on_update(self, dt):

        if self.x <= 300:
            if self.state == 1:
                self.x += 1
                if self.x >= 300:
                    self.state = 0

        return super().on_update(dt)

class Button(Sprite):
    def on_create(self):
        self.color = Color.MAGENTA
        self.scale = 40
        self.add_tag("button")


class Key(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = 40
        self.vy = 0

class Door(Sprite):
    def on_create(self):
        self.color = Color.VERMILION
        self.scale = 80
        self.is_visible = False

class Player(Sprite):
    def on_create(self):
        self.scale = 49
        self.color = Color.VIOLET
        self.y = 100
        self.x = 100
        self.vx = 0
        self.vy = 0
        self.is_on_platform = False
        self.add_tag("player")
        self.layer = 5

    def on_update(self, dt):
        if self.window.is_key_pressed(KeyCode.D):
            self.vx += DV
            if self.vx > MAX_V:
                self.vx = MAX_V
        if self.window.is_key_pressed(KeyCode.A):
            self.vx -= DV
            if self.vx < -MAX_V:
                self.vx = -MAX_V
        if self.window.is_key_down(KeyCode.W) and self.is_on_platform:
            self.vy = JUMP_SPEED
            self.is_on_platform = False

        self.vy -= GRAVITY
        self.vx *= FRCITION

        prev_y = self.y
        prev_x = self.x
        self.x += self.vx
        self.y += self.vy

        platforms = self.window.get_sprites_with_tag("platform")
        for platform in platforms:
            top_y = platform.y + 0.5*(platform.height + self.height)
            bot_y = platform.y - 0.5*(platform.height + self.height)
            if self.is_touching_sprite(platform):
                left_x = platform.x - platform.width/2
                right_x = platform.x + platform.width/2

                if prev_y >= top_y:
                    self.vy = 0
                    self.is_on_platform = True
                    self.y = top_y
                elif prev_y < bot_y:
                    self.vy = 0

                if prev_x <= left_x - self.width/2:
                    self.vx = 0
                    self.x = left_x - self.width/2

                elif prev_x >= right_x + self.width/2:
                    self.vx = 0
                    self.x = right_x + self.width/2