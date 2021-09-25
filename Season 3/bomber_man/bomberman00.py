from pycat.core import Window, Sprite

CELL_SIZE = 48

window = Window(height=700, width=700, is_sharp_pixel_scaling=True)


class Wall(Sprite):
    def on_create(self):
        self.scale = 3
        self.image = 'terrain/wall_1.png'
        self.add_tag('wall')


WORLD_SIZE = 11
LEVEL_OFFSET = CELL_SIZE * 2

for i in range(WORLD_SIZE):
    for j in range(WORLD_SIZE):
        if i == 0 or j == 0 or i == WORLD_SIZE-1 or j == WORLD_SIZE-1:
            wall = window.create_sprite(Wall)
            wall.x = LEVEL_OFFSET + j*CELL_SIZE
            wall.y = LEVEL_OFFSET + i*CELL_SIZE

window.run()
