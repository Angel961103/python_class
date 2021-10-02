from pycat.core import Window, Sprite, KeyCode, RotationMode, Scheduler
from random import random

from pyglet.image import create

CELL_SIZE = 48
TREE_PROB = 0.95

window = Window(height=700, width=700, is_sharp_pixel_scaling=True)


class Wall(Sprite):
    def on_create(self):
        self.scale = 2.8
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

class Explosion(Sprite):
    def on_create(self):
        self.layer = 5
        self.image = "explosion_gifs/center.gif"
        Scheduler.wait(1, self.delete)

class Bomb(Sprite):
    def on_create(self):
        self.scale = 3
        self.layer = 5
        self.image = "bomb.gif"
        Scheduler.wait(1, self.explosion)
        Scheduler.wait(1, self.delete)

    def explosion(self):
        explosion = window.create_sprite(Explosion)
        explosion.position = self.position
        new_explosion = window.create_sprite(Explosion)
        new_explosion.position = explosion.position
        new_explosion.y += CELL_SIZE
        new_explosion.opacity = 0
        new_explosion.image = "explosion_gifs/middle.gif"
        new_explosion.rotation = 90
        new_explosion.opacity = 0
        if new_explosion.is_touching_any_sprite_with_tag("wall"):
            new_explosion.delete()
        else:
            new_explosion.opacity = 225


class Player(Sprite):
    def on_create(self):
        self.image = "player/front.png"
        self.scale = 2.8
        self.layer = 6
        self.x = LEVEL_OFFSET+CELL_SIZE
        self.y = self.x
        self.rotation_mode = RotationMode.NO_ROTATION
        self.delete_neighboring_tree()

    def delete_tree(self):
        for tree in window.get_sprites_with_tag("tree"):
            if self.is_touching_sprite(tree):
                tree.delete()

    def delete_neighboring_tree(self):
        self.delete_tree()
        self.y += CELL_SIZE
        self.delete_tree()
        self.y -= CELL_SIZE
        self.x += CELL_SIZE
        self.delete_tree()
        self.x -= CELL_SIZE

    def rotate_and_move(self, rotate):
            self.rotation = rotate
            self.move_forward(CELL_SIZE)
            if self.is_touching_any_sprite_with_tag("wall"):
                self.move_forward(-CELL_SIZE)
            if self.is_touching_any_sprite_with_tag("tree"):
                self.move_forward(-CELL_SIZE)

    def on_update(self, dt):
        if window.is_key_down(KeyCode.UP):
            self.rotate_and_move(90)
        if window.is_key_down(KeyCode.DOWN):
            self.rotate_and_move(270)
        if window.is_key_down(KeyCode.LEFT):
            self.rotate_and_move(180)
        if window.is_key_down(KeyCode.RIGHT):
            self.rotate_and_move(360)


        if window.is_key_down(KeyCode.SPACE):
            b = window.create_sprite(Bomb)
            b.position = self.position

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
