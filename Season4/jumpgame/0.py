from enum import Enum, auto
from pycat.core import Window, Color, Sprite, KeyCode
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller


window = Window(width=17*32, height=12*32)

ldtk_file = LdtkFile('jumping_levels2.ldtk')
ldtk_file.render_level(window, 'Level_0',debug_tags=True)


class Player(Sprite):

    class State(Enum):
        
        WALK = auto()
        JUMP_UP = auto()
        JUMP_DOWN = auto()

    MAX_SCALE = 60
    MIN_SCALE = 30
    JUMP_SPEED = 2

    def on_create(self):
        self.movement_controller = Controller(window, speed_factor=25)
        self.layer = 10
        self.scale = 30
        self.color = Color.ORANGE
        self.state = Player.State.WALK
    def on_update(self, dt):
        self.position += self.movement_controller.get_movement_delta(dt)

        if self.state is Player.State.WALK:
            if window.is_key_down(KeyCode.SPACE):
                self.state = Player.State.JUMP_UP
        elif self.state is Player.State.JUMP_UP:
            self.scale += Player.JUMP_SPEED
            if self.scale > Player.MAX_SCALE:
                self.state = Player.State.JUMP_DOWN
        elif self.state is Player.State.JUMP_DOWN:
            self.scale -= Player.JUMP_SPEED
            if self.scale < Player.MIN_SCALE:
                self.scale = Player.MIN_SCALE
                self.state = Player.State.WALK


player = window.create_sprite(Player)

window.run()
