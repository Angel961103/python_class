from pycat.window import Window
from platformer import Player, Platform, MovingPlatform, Door, Key, GRAVITY, Button, Key1, Door1

# class Key1(Key):
#     def on_create(self):
#         super().on_create()
#         self.add_tag("key1")
#         self.x = level1.keyplatform.x 
#         self.y = level1.keyplatform.y + self.height/2 + level1.keyplatform.height/2 - 1

#     def on_update(self, dt):
#         if not self.is_touching_sprite(level1.keyplatform):
#             prev_y = self.y
#             self.y += self.vy
#             self.vy -= GRAVITY/2
#             platforms = w.get_sprites_with_tag("platform")
#             for platform in platforms:
#                 top_y = platform.y + 0.5*(platform.height + self.height)
#                 bot_y = platform.y - 0.5*(platform.height + self.height)
#                 if self.is_touching_sprite(platform):
#                     if prev_y >= top_y:
#                         self.vy = 0
#                         self.is_on_platform = True
#                         self.y = top_y

# class Door1(Door):
#     def on_create(self):
#         super().on_create()
#         self.y = 300 + level1.keyplatform.height/2 + self.height/2
#         self.add_tag("door")

#     def on_update(self, dt):
#         if self.is_touching_any_sprite_with_tag("player"):
#             level1.destroy()
#             global level2
#             level2 = Level2()
#             level2.set_up()

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
        w.create_sprite(Button,x=w.width-25, y=70)

    def set_up(self):

        self.keyplatform = self.w.create_sprite(MovingPlatform, x=self.w.center.x-500, y=500)
        self.w.create_sprite(Key1)
        self.door = self.w.create_sprite(Door1, x=self.w.center.x+500)  

    def destroy(self):
        self.w.delete_all_sprites()