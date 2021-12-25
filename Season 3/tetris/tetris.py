from enum import Enum, auto
from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from typing import List

w = Window()

GROUND_Y = 100

class Cell(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = 30
        self.x = 600
        self.y = 600
        self.y_speed = 30
        self.x_speed = 35
        self.time = 0
        self.add_tag("cell")
        self.state = Cell.State.FALL

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
        if w.is_key_up(KeyCode.S):
            while not self.is_touching_any_sprite_with_tag("cell"):
                self.y -= self.y_speed
                if self.y <= GROUND_Y:
                    self.lock()
                self.y = GROUND_Y
                w.create_sprite(Cell)
                break
            self.lock()
            return True
        return False

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
            self.y = cells[0].y + self.height + 5
            self.lock()
            w.create_sprite(Cell)

    def on_update(self, dt):
        if self.state == Cell.State.FALL:
            self.time += dt
            if self.time > 0.5:
                self.y -= self.y_speed
                self.time = 0
        self.left()
        self.right()
        if self.down():
            return
        if self.check_cell():
            return
        self.check_ground()
            

w.create_sprite(Cell)
w.run()