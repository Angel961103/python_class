from numpy import ndarray
from pycat.core import Window, Sprite, Color
from pycat.base import NumpyImage as np
from pycat.base import Texture
from pycat.base.event import MouseEvent
from typing import List, TypeVar

w = Window(is_sharp_pixel_scaling=True)
w.set_clear_color(100, 100, 100)

def sprite_array(row, col, file):
    array = np.get_array_from_file(file)
    m, n, _ = array.shape
    di = m // row
    dj = n // col
    result = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(array[i*di:(i+1)*di, j*dj:(j+1)*dj, :])
        result.append(row)
    return result

def create(w:Window,
           sub_array:List[List[ndarray]],
           scale=1,
           sprite_cls=Sprite):
    s, n = len(sub_array), len(sub_array[0])
    grid: List[List[Sprite]] = []
    for i in range(s):
        row = []
        for j in range(n):
            s = w.create_sprite(sprite_cls)
            s.texture = np.get_texture_from_array(sub_array[i][j])
            s.scale = scale
            s.x = s.width/2 + (j*s.width)
            s.y = s.height/2 + (i*s.height)
            row.append(s)
        grid.append(row)

def create_sprite_grid(
           w:Window,
           x0,
           y0,
           m,
           n,
           scale=1,
           sprite_cls=Sprite):
    grid: List[List[Sprite]] = []
    for i in range(m):
        row = []
        for j in range(n):
            s = w.create_sprite(sprite_cls)
            s.scale = scale
            s.x = x0 + j*(1+s.width)
            s.y = y0 + i*(1+s.height)
            row.append(s)
        grid.append(row)

current_texture: Texture = None

class Level(Sprite):
    def on_create(self):
        pass
    def on_click(self, mouse_event: MouseEvent):
        global current_texture
        width = self.width
        
        self.texture = current_texture
        self.scale_to_width(width)

class Click(Sprite):
    def on_click(self, mouse_event: MouseEvent):
        global current_texture
        current_texture = self.texture

s = sprite_array(9,20,"img/Tilemap/tiles_packed.png")
create(w, s, 1, Click)
create_sprite_grid(w, 500, 100, 10, 10, 50, Level)

w.run()