from pycat.base.base_sprite import RotationMode
from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite

w = Window()
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
        self.width = w.width/6

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

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level1.keyplatform.state = 1

class Button2(Button):
    def on_create(self):
        super().on_create()

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            pass

class Key(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = 40
        print("ok")
        self.vy = 0
        self.add_tag("key")

class Key1(Key):
    def on_create(self):
        super().on_create()
        self.x = level1.keyplatform.x 
        self.y = level1.keyplatform.y + self.height/2 + level1.keyplatform.height/2 - 1

    def on_update(self, dt):
        if not self.is_touching_sprite(level1.keyplatform):
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
class Key2(Key):
    def on_create(self):
        super().on_create()
        self.x = 150
        self.y = 440
        

class Door(Sprite):
    def on_create(self):
        self.color = Color.VERMILION
        self.scale = 80
        self.y = 300 + level1.keyplatform.height/2 + self.height/2
        self.is_visible = False
        self.add_tag("door")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level1.destroy()
            Level2()

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
        prev_x = self.x
        self.x += self.vx
        self.y += self.vy

        platforms = w.get_sprites_with_tag("platform")
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

        if self.is_touching_any_sprite_with_tag("key"):
            level1.door.is_visible = True


class Level1():
    def __init__(self):
        self.player = w.create_sprite(Player)
        self.ground = w.create_sprite(Platform, x=w.center.x, y=25)
        self.ground.width = w.width
        self.ground.height = 50


        w.create_sprite(Platform, x=w.center.x, y=225)
        w.create_sprite(Platform, x=w.center.x+500, y=300)
        w.create_sprite(Platform, x=w.center.x-300, y=150)
        w.create_sprite(Button,x=w.width-25, y=70)

    def set_up(self):

        self.keyplatform = w.create_sprite(MovingPlatform, x=w.center.x-500, y=500)
        # self.keyplatform.add_tag("keyplatform")
        w.create_sprite(Key1)
        self.door = w.create_sprite(Door, x=w.center.x+500)  

    def destroy(self):
        w.delete_all_sprites()


class Level2():
    def __init__(self):
        self.player = w.create_sprite(Player)
        self.ground = w.create_sprite(Platform, x=w.center.x, y=25)
        self.ground.width = w.width
        self.ground.height = 50


        w.create_sprite(Platform, x=300, y=125)
        w.create_sprite(Platform, x=600, y=125)
        w.create_sprite(Platform, x=900, y=125)
        w.create_sprite(Platform, x=150, y=260)
        w.create_sprite(Platform, x=500, y=260)
        w.create_sprite(Platform, x=800, y=260)
        w.create_sprite(Platform, x=1100, y=260)
        w.create_sprite(Platform, x=100, y=390)
        w.create_sprite(Platform, x=600, y=390)
        w.create_sprite(Platform, x=900, y=390)
        w.create_sprite(Button2, x=650, y=435)

    def set_up(self):
        self.keyplatform = w.create_sprite(MovingPlatform, x=200, y=472)
        width, height = self.keyplatform.width, self.keyplatform.height
        self.keyplatform.width, self.keyplatform.height = height, width
        self.keyplatform.add_tag("keyplatform")
        w.create_sprite(Key2)
        # self.door = w.create_sprite(Door, x=w.center.x+500)  

    def destroy(self):
        w.delete_all_sprites()

# level1 = Level1()
# level1.set_up()

level2 = Level2()
level2.set_up()


w.run()