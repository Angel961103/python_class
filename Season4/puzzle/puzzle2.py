from pycat.core import Window, Sprite
from pycat.base import NumpyImage
from pycat.base.event import MouseEvent

w = Window()

class Draggable(Sprite):
    current = None

    def on_create(self):
        w.subscribe(on_mouse_drag=self.on_mouse_drag,
                    on_mouse_release=self.on_mouse_release)

    def on_mouse_drag(self, mouse_event: MouseEvent):
        if Draggable.current is self:
            self.position = mouse_event.position
        

    def on_click(self, mouse_event: MouseEvent):
        Draggable.current = self

    def on_mouse_release(self, mouse_event: MouseEvent):
        Draggable.current = None

def get_image_grid(image_file, rows, cols):
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
            s = w.create_sprite(Draggable, x=(min_j+max_j)/2, y=(min_i+max_i)/2)
            s.texture = NumpyImage.get_texture_from_array(sub)
            s.scale = 0.8
            row.append(s)
        grid.append(row)
    return grid


grid = get_image_grid("view.PNG", 2, 2)
w.run()