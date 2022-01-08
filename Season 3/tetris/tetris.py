from enum import Enum, auto
from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from typing import List

w = Window()
TOP_Y = 600
GAP = 3
SCALE = 30
ROWS = 18
GROUND_Y = TOP_Y-(ROWS-1)*(GAP+SCALE)

class Cell(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = SCALE
        self.x = 600
        self.y = TOP_Y
        self.y_speed = SCALE+GAP
        self.x_speed = SCALE+GAP
        self.time = 0
        self.add_tag("cell")
        self.state = Cell.State.FALL
        self.move_time = 0.5

    class State(Enum):
        FALL = auto()
        LOCKED = auto()

    def lock(self):
        self.state = Cell.State.LOCKED
    
    def left(self):
        if w.is_key_up(KeyCode.A):
            self.x -= self.x_speed
            if self.is_touching_any_sprite_with_tag("cell"):
                self.x += self.x_speed

    def right(self):
        if w.is_key_up(KeyCode.D):
            self.x += self.x_speed
            if self.is_touching_any_sprite_with_tag("cell"):
                self.x -= self.x_speed

    def down(self):
        if w.is_key_pressed(KeyCode.S):
            self.move_time = 0.1
        else:
            self.move_time = 0.5

    def check_ground(self):
        if self.y < GROUND_Y:
            self.lock()
            self.y = GROUND_Y
            w.create_sprite(Cell)
            return True
        else:
            return False

    def check_cell(self):
        cells: List[Cell] = self.get_touching_sprites_with_tag("cell")
        if cells:
            self.y = cells[0].y + self.height + GAP
            self.lock()
            w.create_sprite(Cell)

    def on_update(self, dt):
        if self.state is Cell.State.FALL:
            self.time += dt
            if self.time > self.move_time:
                self.y -= self.y_speed
                self.time = 0
            self.left()
            self.right()
            self.down()
            self.check_cell()
            self.check_ground()
            

w.create_sprite(Cell)
w.run()