from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from pyglet.window import key

w = Window()
DV = 2
MAX_V = 20
FRCITION = 0.88
JUMP_SPEED = 17
GRAVITY = 1

class Platform(Sprite):
    def on_create(self):
        self.color = Color.AZURE
        self.add_tag("platform")
        self.height = 50
        self.width = w.width/6

class MovingPlatform(Platform):
    def on_create(self):
        self.state = 0
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
        self.x = w.width - 25
        self.y = 70
        self.scale = 40
        self.add_tag("button")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            keyplatform.state = 1

class Key(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = 40
        self.x = keyplatform.x 
        self.y = keyplatform.y + self.height/2 + keyplatform.height/2 - 1
        self.vy = 0
        self.add_tag("key")

    def on_update(self, dt):
        if not self.is_touching_sprite(keyplatform):
            prev_y = self.y
            self.y += self.vy
            self.vy -= GRAVITY/2
            platforms = w.get_sprites_with_tag("platform")
            for platform in platforms:
                top_y = platform.y + 0.5*(platform.height + self.height)
                bot_y = platform.y - 0.5*(platform.height + self.height)
                if self.is_touching_sprite(platform):
                    if prev_y >= top_y:
                        self.vy = 0
                        self.is_on_platform = True
                        self.y = top_y

class Door(Sprite):
    def on_create(self):
        self.color = Color.VERMILION
        self.scale = 80
        self.y = 300 + keyplatform.height/2 + self.height/2
        self.is_visible = False

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            w.close()

class Player(Sprite):
    def on_create(self):
        self.scale = 60
        self.color = Color.VIOLET
        self.y = 100
        self.x = 100
        self.vx = 0
        self.vy = 0
        self.is_on_platform = False
        self.add_tag("player")

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
            if self.is_touching_sprite(platform):
                if prev_y >= top_y:
                    self.vy = 0
                    self.is_on_platform = True
                    self.y = top_y
                elif prev_y < bot_y:
                    self.vy = 0
        if self.is_touching_any_sprite_with_tag("key"):
            door.is_visible = True
    

w.create_sprite(Player)
ground = w.create_sprite(Platform, x=w.center.x, y=25)
ground.width = w.width
ground.height = 50


w.create_sprite(Platform, x=w.center.x, y=225)
w.create_sprite(Platform, x=w.center.x+500, y=300)
w.create_sprite(Platform, x=w.center.x-300, y=150)
w.create_sprite(Button)
keyplatform = w.create_sprite(MovingPlatform, x=w.center.x-500, y=500)
w.create_sprite(Key)
door = w.create_sprite(Door, x=w.center.x+500)

w.run()