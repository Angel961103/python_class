from enum import Enum, auto
from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from typing import List
from shapes import S, Z, I, O, J, L, T
from random import choice

w = Window()
TOP_Y = 500
GAP = 3
SCALE = 30
ROWS = 15
GROUND_Y = TOP_Y-(ROWS-1)*(GAP+SCALE)

SHAPES = [S, Z, I, O, J, L, T]

class Game(Sprite):
    def on_create(self):
        self.is_visible = False
        self.shape = Shape()
        

    def left(self):
        for cell in self.shape.cells:
            if cell.state is Cell.State.FALL:
                cell.x -= cell.x_speed

    def right(self):
        for cell in self.shape.cells:
            if cell.state is Cell.State.FALL:
                cell.x += cell.x_speed

    def check_ground(self):
        dy = -1
        for cell in self.shape.cells:
            if cell.y < GROUND_Y:
                dy = GROUND_Y - cell.y
                break
        if dy >= 0:
            for cell in self.shape.cells:
                cell.y += dy
                cell.lock()
            self.shape = Shape()
            

    def on_update(self, dt):
        
        if w.is_key_up(KeyCode.A):
            self.left()
        if w.is_key_up(KeyCode.D):
            self.right()
        self.check_ground()
        # is_lock = False
        # for cell in self.cells:
        #     if cell.check_ground():
        #         is_lock = True
        #         break
        # if is_lock:
        #     for cell in self.cells:
        #         cell.state = Cell.State.LOCKED




class Shape:
    def __init__(self):
        self.string = choice(SHAPES)
        self.x = 600
        self.y = TOP_Y
        x = self.x
        y = self.y
        print(self.string)
        self.cells: List[Cell] = []
        for string in self.string[0]:
            for c in string:
                if c == "0":
                    self.cells.append(w.create_sprite(Cell, x=x, y=y))
                    
                x += GAP+SCALE
            x = self.x
            y -= GAP+SCALE

class Cell(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = SCALE
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
    
    

    def down(self):
        if w.is_key_pressed(KeyCode.S):
            self.move_time = 0.1
        else:
            self.move_time = 0.5

    def check_ground(self):
        if self.y < GROUND_Y:
            self.lock()
            self.y = GROUND_Y
            return True
        else:
            return False

    def check_cell(self):
        cells: List[Cell] = self.get_touching_sprites_with_tag("cell")
        if cells:
            self.y = cells[0].y + self.height + GAP
            self.lock()
            

    def on_update(self, dt):
        if self.state is Cell.State.FALL:
            self.down()
            self.time += dt
            if self.time > self.move_time:
                self.y -= self.y_speed
                self.time = 0
            
            
            

w.create_sprite(Game)
w.run()