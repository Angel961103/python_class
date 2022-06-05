from enum import Enum, auto
from pycat.core import Window, Color, Sprite, KeyCode
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller
from os.path import dirname
from pycat.experimental.spritesheet import SpriteSheet
from pycat.experimental.animation import Animator


window = Window(width=17*32, height=12*32)

ldtk_file = LdtkFile(dirname(__file__) + '/jumping_levels2.ldtk')
ldtk_file.render_level(window, 'Level_0')

class Player(Sprite):

    class State(Enum):
        WALK = auto()
        JUMP = auto()

    MIN_SCALE = 0.5
    G = -3
    JUMP_TIME = 1

    def set_scale(self):
        self.scale = Player.MIN_SCALE + Player.G * self.time * (self.time - Player.JUMP_TIME)

    def on_create(self):
        self.movement_controller = Controller(window, speed_factor=25)
        self.layer = 10
        self.scale = Player.MIN_SCALE
        self.color = Color.ORANGE
        self.state = Player.State.WALK
        self.time = 0
        self.start = window.get_sprites_with_tag("player_start")[0]
        self.position = self.start.position
        self.sprite_sheet = SpriteSheet('player.png', 64, 64)
        self.walk_texture_left = [self.sprite_sheet.get_texture(x,2, True) for x in range(4)]
        self.walk_texture_right = [self.sprite_sheet.get_texture(x,2) for x in range(4)]
        self.walk_texture_front = [self.sprite_sheet.get_texture(x,1) for x in range(4)]
        self.walk_texture_back = [self.sprite_sheet.get_texture(x,3) for x in range(4)]

        self.animator = Animator()
        self.animator.add('left', self.walk_texture_left)
        self.animator.add('right', self.walk_texture_right)
        self.animator.add('front', self.walk_texture_front)
        self.animator.add('back', self.walk_texture_back)
        self.animator.play('front')

    def on_update(self, dt):
        self.texture = self.animator.tick(dt)
        self.position += self.movement_controller.get_movement_delta(dt)

        if self.state is Player.State.WALK:
            if window.is_key_down(KeyCode.SPACE):
                self.state = Player.State.JUMP
                self.time = 0
            if self.is_touching_any_sprite_with_tag("land"):
                pass
            else:
                self.position = self.start.position
            
            if window.is_key_down(KeyCode.W):
                self.animator.play('back')
            if window.is_key_down(KeyCode.S):
                self.animator.play('front')

        if self.state is Player.State.JUMP:
            self.set_scale()
            self.time += dt

            if self.time > Player.JUMP_TIME:
                self.scale = Player.MIN_SCALE
                self.state = Player.State.WALK
                if not self.is_touching_any_sprite_with_tag("land"):
                    self.position = self.start.position

player = window.create_sprite(Player)

window.run()