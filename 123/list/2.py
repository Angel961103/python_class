from typing import List
from pycat.base.color import Color
from pycat.core import Window, Sprite
from pyglet.gl.glext_arb import GL_EXT_x11_sync_object

ROW = 6
COL = 10
CELL_SIZE = 100

w = Window(width=COL*CELL_SIZE, height=ROW*CELL_SIZE)

class Cell(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE - 1
        self.color = Color.RED

    def set_ij(self,i, j):
        self.i = i
        self.j = j

    def change_color(self):
        if self.color == Color.GREEN:
            self.color = Color.RED
        else:
            self.color = Color.GREEN

    def change_neighbors(self):
        i = self.i
        j = self.j
        if i > 0:
            grid[i-1][j].change_color()
        if i+1 < ROW:
            grid[i+1][j].change_color()
        if j > 0:
            grid[i][j-1].change_color()
        if j+1 < COL:
            grid[i][j+1].change_color()

    def check_for_win(self):
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == Color.GREEN:
                    return
        print("you win")

    def on_left_click(self):
        self.change_neighbors()
        self.check_for_win()

x0 = y0 = CELL_SIZE/2
grid: List[List[Cell]] = []
for i in range(ROW):
    my_row = []
    for j in range(COL):
        c = w.create_sprite(Cell)
        c.x = x0 + j*CELL_SIZE
        c.y = y0 + i*CELL_SIZE
        c.set_ij(i,j)
        my_row.append(c)
    grid.append(my_row)

grid[2][2].change_neighbors()

w.run()