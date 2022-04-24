from pycat.core import Window, Sprite, KeyCode, Color
from pycat.base import NumpyImage as np
from pycat.base import Texture, MouseEvent, MouseButton
from typing import List, Callable, TypeVar


class SelectionCell(Sprite):
    def on_left_click(self):
        global current_texture
        current_texture = self.texture
        print("selected texture")


class LevelCell(Sprite):
    def on_create(self):
        w.subscribe(on_mouse_drag=self.on_mouse_drag)

    def on_mouse_drag(self, m: MouseEvent):
        if self.contains_point(m.position):
            width = self.width
            if m.button is MouseButton.LEFT:
                if current_texture:
                    self.texture = current_texture
                    self.scale_to_width(width)
            else:
                self.texture = None
                self.color = Color.WHITE
                self.scale_to_width(width)


class SpriteGrid:

    T = TypeVar('T', bound=Sprite)

    def __init__(self,
                 rows: int,
                 cols: int,
                 x: float = None,
                 y: float = None,
                 scale: float = 10,
                 cell_gap: float = 1,
                 cell_cls: Callable[..., T] = Sprite):

        self.__x = scale/2 if x is None else x
        self.__y = scale/2 if y is None else y
        self.__scale = scale
        self.__cell_gap = cell_gap
        self.__rows = rows
        self.__cols = cols
        self.__cells = [[w.create_sprite(cell_cls) for j in range(cols)]
                        for i in range(rows)]
        self.__update_cells()

    def __update_cells(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                s = self.__cells[i][j]
                s.scale_to_width(self.scale)
                s.x = self.x + (s.width+self.cell_gap)*j
                s.y = self.y + (s.height+self.cell_gap)*i

    def split_sprite_sheet(self, file: str):
        self.array = np.get_array_from_file(file)
        m, n, _ = self.array.shape  # pixels
        di = m // self.rows
        dj = n // self.cols
        sub_arrays = [[self.array[i*di:(i+1)*di, j*di:(j+1)*dj, :]
                      for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.__cells[i][j]
                cell.texture = np.get_texture_from_array(sub_arrays[i][j])
                cell.scale_to_width(self.scale)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val: float):
        self.__x = val
        self.__update_cells()

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val: float):
        self.__y = val
        self.__update_cells()

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, val: float):
        self.__scale = val
        self.__update_cells()

    @property
    def cell_gap(self):
        return self.__cell_gap

    @cell_gap.setter
    def cell_gap(self, val: float):
        self.__cell_gap = val
        self.__update_cells()

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols


w = Window(is_sharp_pixel_scaling=True)
current_texture: Texture = None
selection_grid = SpriteGrid(rows=7, cols=12, scale=30, cell_cls=SelectionCell)
selection_grid.split_sprite_sheet('pattern.png')
level_grid = SpriteGrid(rows=20, cols=40, scale=15, x=600, cell_gap=1,
                        cell_cls=LevelCell)


class GridController(Sprite):
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.W):
            level_grid.y += 5
        if w.is_key_pressed(KeyCode.S):
            level_grid.y -= 5
        if w.is_key_pressed(KeyCode.A):
            level_grid.x -= 5
        if w.is_key_pressed(KeyCode.D):
            level_grid.x += 5
        if w.is_key_pressed(KeyCode.UP):
            level_grid.scale *= 1.01
        if w.is_key_pressed(KeyCode.DOWN):
            level_grid.scale *= 0.99


w.create_sprite(GridController)
w.run()
