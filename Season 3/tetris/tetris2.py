from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
from typing import List
from shapes import S, Z, I, O, J, L, T, shape_colors
from random import choice, randint

w = Window()
TOP_Y = 500
LEFT_X = 200
GAP = 3
SCALE = 20
ROWS = 25
COLS = 15
GROUND_Y = TOP_Y-(ROWS-1)*(GAP+SCALE)
NORMAL_FALL_TIME = 0.5
FAST_FALL_TIME = 0.1

SHAPES = [S, Z, I, O, J, L, T]
grid = [None for j in range(COLS) for i in range(ROWS)]

class Game(Sprite):
    def on_create(self):
        self.is_visible = False
        self.shape = Shape()
        self.time = 0
        self.grid: List[List[Cell]] = [[None for j in range(COLS)] for i in range(ROWS)]
        self.fall_time = NORMAL_FALL_TIME
        for i in range(ROWS):
            for j in range(COLS):
                c = w.create_sprite(Cell, layer=-1, color=Color.WHITE)
                c.i = i
                c.j = j
                c.set_grid_position()

    def is_under_ground(self):
        for c in self.shape.cells:
            if c.i >= ROWS:
                return True

    def is_touching_left(self):
        for c in self.shape.cells:
            if c.j < 0:
                return True

    def is_touching_right(self):
        for c in self.shape.cells:
            if c.j >= COLS:
                return True

    def lock_shape(self):
        for c in self.shape.cells:
            self.grid[c.i][c.j] = c

    def is_touching_locked(self):
        for c in self.shape.cells:
            if self.grid[c.i][c.j]:
                return True

    def check_rows(self):
        i = ROWS-1
        while i >= 0:
            is_full = True
            for j in range(COLS):
                if self.grid[i][j] is None:
                    is_full = False
            if is_full:
                for cell in self.grid[i]:
                    cell.delete()
                self.move_grid_down(i)    
            i -= 1

    def move_grid_down(self, row):
        for i in range(row-1, -1, -1):
            for j in range(COLS):
                c = self.grid[i][j]
                if c is not None:
                    self.grid[i+1][j] = c
                    c.i = i+1
                    c.set_grid_position()
        self.grid[0] = [None]*COLS

    def on_update(self, dt):
        self.time += dt
        if w.is_key_pressed(KeyCode.S):
            self.fall_time = FAST_FALL_TIME
        else:
            self.fall_time = NORMAL_FALL_TIME
        if self.time > self.fall_time:
            self.time = 0
            self.shape.move_down()
            if self.is_under_ground() or self.is_touching_locked():
                self.shape.move_up()
                self.lock_shape()
                self.check_rows()
                self.shape = Shape()
                if self.is_touching_locked():
                    w.close()
        if w.is_key_down(KeyCode.A):
            self.shape.move_left()
            if self.is_touching_left() or self.is_touching_locked():
                self.shape.move_right()
        if w.is_key_down(KeyCode.D):
            self.shape.move_right()
            if self.is_touching_right() or self.is_touching_locked():
                self.shape.move_left()
        if w.is_key_down(KeyCode.SPACE):
            self.shape.rotate()

class Shape:
    def __init__(self):
        self.index = randint(0,len(SHAPES)-1)
        self.rotation_strings = SHAPES[self.index]
        self.color = shape_colors[self.index]
        self.i = 0
        self.j = 5
        self.cells: List[Cell] = []
        self.rotation_index = choice(range(len(self.rotation_strings)))
        self.make_cells()

    def make_cells(self):
        s = self.rotation_strings[self.rotation_index]
        rows = len(s)
        cols = len(s[0])
        for i in range(rows):
            for j in range(cols):
                if s[i][j] == "0":
                    cell = w.create_sprite(Cell)
                    cell.i = self.i + i
                    cell.j = self.j + j
                    cell.set_grid_position()
                    cell.color = self.color
                    self.cells.append(cell)

    def delete_cells(self):
        for c in self.cells:
            c.delete()
        self.cells.clear()

    def rotate(self, direction: int=1):
        self.delete_cells()
        self.rotation_index += direction
        self.rotation_index %= len(self.rotation_strings)
        self.make_cells()

    def move_down(self):
        self.i += 1
        self.update_cells(1, 0)

    def move_up(self):
        self.i -= 1
        self.update_cells(-1, 0)

    def update_cells(self, di, dj):
        for cell in self.cells:
            cell.i += di
            cell.j += dj
            cell.set_grid_position()

    def move_right(self):
        self.j += 1
        self.update_cells(0, 1)

    def move_left(self):
        self.j -= 1
        self.update_cells(0, -1)


class Cell(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.scale = SCALE - 1
        self.i = None
        self.j = None

    def set_grid_position(self):
        self.x = LEFT_X + self.j * SCALE
        self.y = TOP_Y - self.i * SCALE   

w.create_sprite(Game)
w.run()