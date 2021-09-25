from pycat.core import Window, Sprite
from random import random

from pyglet.image import create

CELL_SIZE = 48
TREE_PROB = 0.15

window = Window(height=700, width=700, is_sharp_pixel_scaling=True)


class Wall(Sprite):
    def on_create(self):
        self.scale = 3
        self.image = 'terrain/wall_1.png'
        self.add_tag('wall')

class Grass(Sprite):
    def on_create(self):
        self.scale = 3
        self.image = 'terrain/grass_1.png'

class Tree(Sprite):
    def on_create(self):
        self.scale = 3
        self.image = 'terrain/tree.png'
        self.layer = 5
        self.add_tag("tree")

class Player(Sprite):
    def on_create(self):
        self.image = "player/front.png"
        self.scale = 3
        self.layer = 6
        self.x = LEVEL_OFFSET+CELL_SIZE
        self.y = self.x

        for tree in window.get_sprites_with_tag("tree"):
            if self.is_touching_sprite(tree):
                tree.delete()

WORLD_SIZE = 11
LEVEL_OFFSET = CELL_SIZE * 2

for i in range(WORLD_SIZE):
    for j in range(WORLD_SIZE):
        x = LEVEL_OFFSET + j*CELL_SIZE
        y = LEVEL_OFFSET + i*CELL_SIZE
        if i == 0 or j == 0 or i == WORLD_SIZE-1 or j == WORLD_SIZE-1:
            wall = window.create_sprite(Wall, x=x, y=y)
        elif i%2 == 0 and j%2 == 0:
            wall = window.create_sprite(Wall, x=x, y=y)
        elif i%2 == 1 or j%2 == 1:
            grass = window.create_sprite(Grass, x=x, y=y)
            if random() < TREE_PROB:
                tree = window.create_sprite(Tree, x=x, y=y)

window.create_sprite(Player)

window.run()
