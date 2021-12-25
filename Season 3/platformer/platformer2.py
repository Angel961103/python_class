from pycat.window import Window, Sprite, Color
from platform_lib import Player, Platform, MovingPlatform, Door, Key, GRAVITY, Button

w = Window()

class Button1(Button):
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level1.keyplatform.state = 1

class Key1(Key):
    def on_create(self):
        super().on_create()
        self.add_tag("key1")
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

        if self.is_touching_any_sprite_with_tag("player"):
            level1.door.is_visible = True


class Key2(Key):
    def on_create(self):
        super().on_create()
        self.x = 150
        self.y = 440
        self.add_tag("key2")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level2.door.is_visible = True       

class Door2(Door):
    def on_create(self):
        super().on_create()
        self.add_tag("door2")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level2.destroy()

class Door1(Door):
    def on_create(self):
        super().on_create()
        self.y = 300 + level1.keyplatform.height/2 + self.height/2
        self.add_tag("door")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            level1.destroy()
            global level2
            level2 = Level2()
            level2.set_up()

class Level1():
    def __init__(self, w: Window):
        self.w = w
        self.player = w.create_sprite(Player)
        self.ground = w.create_sprite(Platform, x=w.center.x, y=25)
        self.ground.width = w.width
        self.ground.height = 50


        w.create_sprite(Platform, x=w.center.x, y=225)
        w.create_sprite(Platform, x=w.center.x+500, y=300)
        w.create_sprite(Platform, x=w.center.x-300, y=150)
        w.create_sprite(Platform, x=w.center.x+300, y=200)
        w.create_sprite(Button1,x=w.width-25, y=70)

    def set_up(self):

        self.keyplatform = self.w.create_sprite(MovingPlatform, x=self.w.center.x-500, y=500)
        self.w.create_sprite(Key1)
        self.door = self.w.create_sprite(Door1, x=self.w.center.x+500)  

    def destroy(self):
        self.w.delete_all_sprites()



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
        self.door = w.create_sprite(Door2, x=w.center.x+300, y=455)  

    def destroy(self):
        w.delete_all_sprites()

class Button2(Button):
    def on_create(self):
        super().on_create()

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            p = w.get_sprites_with_tag("keyplatform")
            if p:
                p[0].delete()

level1 = Level1(w)
level1.set_up()

level2 = None

w.run()