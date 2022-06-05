from pycat.core import Window, Sprite, KeyCode, Color
from pycat.experimental.ldtk_level_entities import get_levels_entities
from enum import Enum, auto

w = Window(width=1000, height=600)
f = "C:/Users/peanuts-english/Documents/python-students/Angel/Season4/final/final.ldtk"

class Level(Sprite):
    def on_create(self):
        self.position = w.center
        self.image = "png/Level_0.png"
        self.layer = -1
        for g in get_levels_entities(f)[0].entities:
            w.create_sprite(x=g.x, y=g.y, scale_x=g.width, scale_y=g.height, tags=g.tags, opacity=55)

DV = 2
MAX_V = 10
JUMP_SPEED = 17
FRCITION = 0.78
GRAVITY = 1

class Player(Sprite):
    GRAVITY = -0.9
    JUMP_VELOCITY = 15
    FRICTION = 0.9
    MAX_SPEED = 20
    ACCELERATION = 1.
    CLIMB_SPEED = 4

    class State(Enum):
        STANDING = auto()
        WALKING = auto()
        JUMPING = auto()
        FALLING = auto()
        CLIMBING = auto()

    def on_create(self):
        self.image = "png/character_0001.png"
        self.y = 200
        self.x = 100
        self.vx = 0
        self.vy = 0
        self.dy = 0
        self.dx = 0
        self.is_on_platform = False
        self.add_tag("player")
        self.layer = 5
        self.state = Player.State.STANDING

    def is_on_a_ladder(self):
        return bool(self.get_touching_sprites_with_tag('l'))
        
    def is_on_top_of_ladder(self):
        ladders = self.get_touching_sprites_with_tag('l')
        return self.y > ladders[0].y if ladders else False
    
    def is_on_bottom_of_ladder(self):
        ladders = self.get_touching_sprites_with_tag('l')
        return self.y < ladders[0].y if ladders else False

    def walk(self):
        if w.is_key_pressed(KeyCode.D):
            self.vx += DV
            if self.vx > MAX_V:
                self.vx = MAX_V
            self.state = Player.State.WALKING
        if w.is_key_pressed(KeyCode.A):
            self.vx -= DV
            if self.vx < -MAX_V:
                self.vx = -MAX_V
            self.state = Player.State.WALKING

    def on_update(self, dt):

        if self.state is Player.State.STANDING:
            if not self.is_touching_any_sprite_with_tag("g"):
                self.state = Player.State.FALLING
            self.walk()
            if w.is_key_down(KeyCode.W):
                self.vy = JUMP_SPEED
                self.state = Player.State.JUMPING
            
        elif self.state is Player.State.WALKING:
            self.x += self.vx
            self.walk()
            self.vx *= FRCITION
            if w.is_key_down(KeyCode.W):
                self.vy = JUMP_SPEED
                self.state = Player.State.JUMPING
        elif self.state is Player.State.FALLING:
            self.y += self.vy
            self.vy -= GRAVITY
            g = w.get_sprite_with_tag("g")
            if g:
                self.y = g.y + g.height/2 + self.height/2
                self.state = Player.State.STANDING 
        elif self.state is Player.State.JUMPING:
            self.y += self.vy
            self.vy -= GRAVITY
            if self.vy < 0:
                self.state = Player.State.FALLING
                
        # if w.is_key_pressed(KeyCode.D):
        #     self.vx += DV
        #     if self.vx > MAX_V:
        #         self.vx = MAX_V
        # if w.is_key_pressed(KeyCode.A):
        #     self.vx -= DV
        #     if self.vx < -MAX_V:
        #         self.vx = -MAX_V
        # if w.is_key_down(KeyCode.W) and self.is_on_platform:
        #     self.vy = JUMP_SPEED
        #     self.is_on_platform = False

        # if w.is_key_down(KeyCode.SPACE):
        #     if self.is_on_a_ladder():
        #         self.dy = self.CLIMB_SPEED
        #         self.dx = 0
        #         self.y += self.dy

        # self.vy -= GRAVITY
        # self.vx *= FRCITION

        # prev_y = self.y
        # prev_x = self.x
        # self.x += self.vx
        # self.y += self.vy

        # platforms = w.get_sprites_with_tag("g")
        # for platform in platforms:
        #     top_y = platform.y + 0.5*(platform.height + self.height)
        #     bot_y = platform.y - 0.5*(platform.height + self.height)
        #     if self.is_touching_sprite(platform):
        #         left_x = platform.x - platform.width/2
        #         right_x = platform.x + platform.width/2

        #         if prev_y >= top_y:
        #             self.vy = 0
        #             self.is_on_platform = True
        #             self.y = top_y
        #         elif prev_y < bot_y:
        #             self.vy = 0

        #         if prev_x <= left_x - self.width/2:
        #             self.vx = 0
        #             self.x = left_x - self.width/2

        #         elif prev_x >= right_x + self.width/2:
        #             self.vx = 0
        #             self.x = right_x + self.width/2

w.create_sprite(Level)
w.create_sprite(Player)
w.run()