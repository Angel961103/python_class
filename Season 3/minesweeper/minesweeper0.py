from pycat.base.color import Color
from pycat.base.event import MouseEvent, MouseButton
from pycat.core import Window, Sprite
from typing import List, Tuple
from random import random

w = Window()

X0 = Y0 = 100
ROWS = 10
COLS = 10
CELL_SIZE = 50

class Cell(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-1
        self.color = Color.AMBER
        self.bomb = None
        self.label = None
        self.flag = None
        self.i = None
        self.j = None
        self.is_uncovered = False

    def add_label(self, text: str):
        self.label = w.create_label(x=self.x,
                                    y=self.y,
                                    text=text,
                                    font_size=10,
                                    opacity=0)
        self.label.x -= self.label.content_width/2
        self.label.y += self.label.content_height/2

    def add_bomb(self):
        self.bomb = w.create_sprite(x=self.x,
                                    y=self.y,
                                    scale=self.scale/2,
                                    opacity=0,
                                    color=Color.BLUE,
                                    layer=2)

    def add_flag(self):
        self.flag = w.create_sprite(x=self.x,
                                   y=self.y,
                                   scale=self.scale/2,
                                   color=Color.RED,
                                   opacity=0,
                                   layer=4)

    def on_click(self, event: MouseEvent):
        if event.button == MouseButton.RIGHT:
            if self.flag.opacity == 255:
                self.flag.opacity = 0
            else:
                self.flag.opacity = 255
        elif event.button == MouseButton.LEFT:
            
            if not self.bomb and not self.label:
                print("dfs_uncover")
                dfs_uncover(self.i, self.j)
            else:
                self.uncover()               

            
    def uncover(self):
        self.is_uncovered = True
        self.color = Color(100, 100, 100)
        if self.bomb:
            self.bomb.opacity = 255
        if self.label:
            self.label.opacity = 255


def get_neighbors(i: int, j: int)-> List[Tuple[int, int]]:
    return [(i+1,j-1),(i+1,j),(i+1,j+1),
            (i  ,j-1),        (i  ,j+1),
            (i-1,j-1),(i-1,j),(i-1,j+1)]

def count_bombs(i: int, j: int)-> int:
    neighbors = get_neighbors(i, j)
    count = 0
    for i, j in neighbors:
        if (0 <= i < ROWS)and(0 <= j < COLS):
            if grid[i][j].bomb:
                count += 1

    return count


def dfs_uncover(i: int, j: int):
    if not((0 <= i < ROWS)and(0 <= j < COLS)):
        print("1")
        return
    if grid[i][j].is_uncovered:
        print("2")
        return
    if grid[i][j].label:
        grid[i][j].uncover()
        return
    grid[i][j].uncover()
    neighbors = get_neighbors(i, j)
    for i, j in neighbors:
        dfs_uncover(i, j)

grid: List[List[Cell]] = []
for i in range(ROWS):
    row: List[Cell] = []
    for j in range(COLS):
        c = w.create_sprite(Cell)
        c.x = X0 + CELL_SIZE*j
        c.y = Y0 + CELL_SIZE*i
        row.append(c)
        c.add_flag()
        c.i = i
        c.j = j
        if random()<0.05:
            c.add_bomb()
    grid.append(row)


for i in range(ROWS):
    for j in range(COLS):
        c = count_bombs(i,j)
        if c > 0:
            grid[i][j].add_label(str(c))

 
w.run()