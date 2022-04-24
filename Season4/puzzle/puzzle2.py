from turtle import position
from pycat.core import Window, Sprite
from pycat.base import NumpyImage
from pycat.base.event import MouseEvent
from random import shuffle
from typing import List

w = Window()

class Draggable(Sprite):
    current = None

    def on_create(self):
        w.subscribe(on_mouse_drag=self.on_mouse_drag,
                    on_mouse_release=self.on_mouse_release)

    def set_ij(self, i, j):
        self.i = i
        self.j = j

    def on_mouse_drag(self, mouse_event: MouseEvent):
        if Draggable.current is self:
            self.position = mouse_event.position
        
    def on_click(self, mouse_event: MouseEvent):
        Draggable.current = self

    def on_mouse_release(self, mouse_event: MouseEvent):
        Draggable.current = None
        targets = self.get_touching_sprites_with_tag("target")
        if targets:
            self.position = targets[0].position
            check_win()

def check_win():
        for row in grid:
            for p in row:
                t: List[Target] = p.get_touching_sprites_with_tag("target")
                if t:
                    target = t[0]
                    if (target.i != p.i) or (target.j != p.j):
                        return False
                else:
                    return False
        return True
        

def get_image_grid(image_file, rows, cols, x0, y0, scale):
    img = NumpyImage.get_array_from_file(image_file)
    p_rows, p_cols, _ = img.shape
    grid = []
    row_s = p_rows//rows
    col_s = p_cols//cols
    for i in range(rows):
        row = []
        for j in range(cols):
            min_i = i * row_s
            max_i = (i+1) * row_s
            min_j = j * col_s
            max_j = (j+1) * col_s
            sub = img[min_i:max_i, min_j:max_j, :]
            s = w.create_sprite(Draggable)
            t = w.create_sprite(Target)
            s.texture = NumpyImage.get_texture_from_array(sub)
            s.scale = scale
            s.x = x0 + j*(1+s.width)
            s.y = y0 + i*(1+s.height)
            t.x = x0 + j*(1+s.width)
            t.y = y0 + i*(1+s.height)
            s.set_ij(i, j)
            t.set_ij(i, j)
            row.append(s)
        grid.append(row)
    return grid


def randomize():
    positions = []
    for row in grid:
        for p in row:
            positions.append(p.position)
        
    shuffle(positions)
    for row in grid:
        for p in row:
            p.position = positions.pop()

class Target(Sprite):
    def on_create(self):
        self.scale = 50
        self.layer = 1
        self.add_tag("target")

    def set_ij(self, i, j):
        self.i = i
        self.j = j

grid: List[List[Draggable]] = get_image_grid("view.PNG", 2, 2, 500, 300, 0.5)
randomize()
w.run()