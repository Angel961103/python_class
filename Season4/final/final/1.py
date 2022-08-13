from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.ldtk_level_entities import get_levels_entities
from enum import Enum, auto

w = Window(width=1000, height=600)
f = "C:/Users/peanuts-english/Documents/python-students/Angel/Season4/final/final.ldtk"

class Level(Sprite):
    def on_create(self):
        self.position = w.center
        self.image = "png/Level_1.png"
        self.layer = -1
        for g in get_levels_entities(f)[1].entities:
            w.create_sprite(x=g.x, y=g.y, scale_x=g.width, scale_y=g.height, tags=g.tags, opacity=1)

class Key(Sprite):
    def on_create(self):
        self.image = "png/Level_2.png"
        self.x = 370
        self.y = 460
        self.add_tag("Key")
        
    def on_update(self, dt):
        if self.get_touching_sprites_with_tag("player"):
            self.is_visible = False
            g.is_visible = True

class KeyHole(Sprite):
    def on_create(self):
        self.image = "png/Level_5.png"
        self.x = 550
        self.y = 30
        self.add_tag("Keyhole")
        
    def on_update(self, dt):
        if self.get_touching_sprites_with_tag("player"):
            self.is_visible = False
            flag.is_visible = True

class Flag(Sprite):
    def on_create(self):
        self.image = "png/Level_4.png"
        self.x = 980
        self.y = 230
        self.add_tag("flag")
        self.is_visible = False

class Ground(Sprite):
    def on_create(self):
        self.image = "png/Level_3.png"
        self.x = 855
        self.y = 175
        self.is_visible = False
        self.add_tag("g")

w.create_sprite(Key)
w.create_sprite(KeyHole)
g = w.create_sprite(Ground)
flag = w.create_sprite(Flag)

class Player(Sprite):
    GRAVITY = 1.5
    JUMP_VELOCITY = 17
    FRICTION = 0.78
    MAX_SPEED = 10
    ACCELERATION = 1
    CLIMB_SPEED = 2
    SWIM_SPEED = 2
    JUMP_KEY = KeyCode.SPACE

    class State(Enum):
        STANDING = auto()
        WALKING = auto()
        JUMPING = auto()
        FALLING = auto()
        CLIMBING = auto()
        SWIMMING = auto()

    def on_create(self):
        self.image = "character_0001.png"
        self.y = 200
        self.x = 100
        self.vx = 0
        self.vy = 0
        self.dy = 0
        self.dx = 0
        self.is_on_platform = False
        self.add_tag("player")
        self.layer = 5
        self.state = Player.State.FALLING

    def is_on_a_ladder(self):
        return bool(self.get_touching_sprites_with_tag('l'))

    def update_vx(self):
        if w.is_key_pressed(KeyCode.D):
            self.vx += Player.ACCELERATION
            if self.vx > Player.MAX_SPEED:
                self.vx = Player.MAX_SPEED
            
        if w.is_key_pressed(KeyCode.A):
            self.vx -= Player.ACCELERATION
            if self.vx < -Player.MAX_SPEED:
                self.vx = -Player.MAX_SPEED
        self.vx *= Player.FRICTION
        self.x += self.vx
        if abs(self.vx) < 0.2:
            self.vx = 0

    def update_vy(self):
        self.y += self.vy
        self.vy -= Player.GRAVITY

    def on_update(self, dt):

        if self.is_touching_any_sprite_with_tag("flag"):
            w.close()

        if self.state is Player.State.STANDING:
            self.update_vx()
            if self.vx != 0:
                self.state = Player.State.WALKING
            if w.is_key_down(Player.JUMP_KEY):
                self.vy = Player.JUMP_VELOCITY
                self.state = Player.State.JUMPING
            if self.is_on_a_ladder():
                if w.is_key_pressed(KeyCode.UP):
                    self.state = Player.State.CLIMBING

        elif self.state is Player.State.WALKING:
            self.update_vx()
            if self.get_touching_sprites_with_tag("k"):
                self.has_key = True
            if self.get_touching_sprites_with_tag("block"):
                self.x -= self.vx
            if not self.is_touching_any_sprite_with_tag("g"):
                self.state = Player.State.FALLING
                self.vy = 0
            elif self.vx == 0:
                self.state = Player.State.STANDING
            elif w.is_key_down(Player.JUMP_KEY):
                self.vy = Player.JUMP_VELOCITY
                self.state = Player.State.JUMPING

        elif self.state is Player.State.FALLING:
            self.update_vx()
            self.update_vy()
            g = self.get_touching_sprites_with_tag("g")
            if g:
                ground_y = g[0].y + g[0].height/2 + self.height/2
                if self.y - self.vy > ground_y:
                    self.y = ground_y
                    self.state = Player.State.STANDING
            else:
                water = self.get_touching_sprites_with_tag("water")
                if water:
                    water_y = water[0].y + water[0].height/2 - self.height/2
                    if self.y < water_y:
                        self.state = Player.State.SWIMMING
            # TO DO
            # else:
            #     l = self.get_touching_sprites_with_tag("l")
            #     if l:
            #         self.y = l[0].y + l[0].height/2 + self.height/2
            #         self.state = Player.State.STANDING

        elif self.state is Player.State.JUMPING:
            self.update_vx()
            self.update_vy()
            if self.get_touching_sprites_with_tag("jump"):
                self.vy = Player.JUMP_VELOCITY + 10
            if self.get_touching_sprites_with_tag("block"):
                self.vy = 0
                self.vx = 0
            if self.vy < 0:
                self.state = Player.State.FALLING

        elif self.state is Player.State.CLIMBING:
            self.update_vx()
            if self.is_on_a_ladder():
                if w.is_key_pressed(KeyCode.W):
                    self.y += Player.CLIMB_SPEED
                    if not self.is_on_a_ladder():
                        self.state = Player.State.STANDING
                        self.vy = 0
                if w.is_key_pressed(KeyCode.S):
                    self.y -= Player.CLIMB_SPEED
                    if self.is_touching_any_sprite_with_tag("g"):
                        self.state = Player.State.STANDING
                        self.vy = 0
            elif not self.is_on_a_ladder():
                self.state = Player.State.FALLING
                self.vy = 0

        elif self.state is Player.State.SWIMMING:
            self.update_vx()
            if w.is_key_pressed(KeyCode.W):
                self.y += Player.SWIM_SPEED - 1
            if w.is_key_pressed(KeyCode.S):
                self.y -= Player.SWIM_SPEED - 1
            if self.get_touching_sprites_with_tag("g"):
                self.x -= self.vx
            water = self.get_touching_sprites_with_tag("water")
            if not water:
                self.vy = 0
                self.state = Player.State.FALLING
            if water:
                water_y = water[0].y + water[0].height/2 + self.height/2
                self.y -= 0.5
                if self.y > water_y:
                    self.state = Player.State.STANDING

w.create_sprite(Level)
w.create_sprite(Player)
w.run()