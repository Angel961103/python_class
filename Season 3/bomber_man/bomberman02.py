from pycat.core import Window, Sprite, KeyCode, RotationMode, Scheduler
from random import random
from pycat.geometry.point import Point

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
        self.scale = 2.9
        self.image = 'terrain/tree.png'
        self.layer = 5
        self.add_tag("tree")

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("explosion"):
            self.delete()

class Explosion(Sprite):
    def on_create(self):
        self.layer = 5
        self.image = "explosion_gifs/center.gif"
        self.add_tag("explosion")
        Scheduler.wait(1, self.delete)

class PowerUp(Sprite):
    def on_create(self):
        self.layer = 4
        self.image = "powerup_middl.png"
        self.add_tag("power_up")  
        self.scale = 0.5   


class Bomb(Sprite):
    def on_create(self):
        self.scale = 3
        self.layer = 5
        self.image = "bomb.gif"
        self.power = 1
        Scheduler.wait(1, self.explosion)
        Scheduler.wait(1, self.delete)


    

    def explosion(self):
        # center
        explosion = window.create_sprite(Explosion)
        explosion.position = self.position

        def make_explosion(x, y, rotation=0):
            new_explosion = window.create_sprite(Explosion)
            #new_explosion.position = explosion.position
            new_explosion.x = x
            new_explosion.y = y
            new_explosion.image = "explosion_gifs/middle.gif"
            new_explosion.rotation = rotation
            new_explosion.opacity = 0
            if new_explosion.is_touching_any_sprite_with_tag("wall"):
                new_explosion.delete()
                return False
            else:
                new_explosion.opacity = 225
                return True

        for i in range(1, self.power+1):

            if not make_explosion(self.x, self.y+i*CELL_SIZE, 90):
                break

        for i in range(1, self.power+1):

            if not make_explosion(self.x, self.y-i*CELL_SIZE, 90):
                break

        for i in range(1, self.power+1):

            if not make_explosion(self.x+i*CELL_SIZE, self.y):
                break

        for i in range(1, self.power+1):

            if not make_explosion(self.x-i*CELL_SIZE, self.y):
                break
            
class Player(Sprite):
    def on_create(self):
        self.image = "player/front.png"
        self.scale = 2.8
        self.layer = 6
        self.x = LEVEL_OFFSET+CELL_SIZE
        self.y = self.x
        self.rotation_mode = RotationMode.NO_ROTATION
        self.power = 1
        self.delete_neighboring_tree()
        

    def delete_tree(self):
        for tree in window.get_sprites_with_tag("tree"):
            if self.is_touching_sprite(tree):
                tree.delete()

    def delete_p(self):
        for p in window.get_sprites_with_tag("power_up"):
            if self.is_touching_sprite(p):
                p.delete()
                

    def delete_neighboring_tree(self):
        offsets = [Point(CELL_SIZE,0),
                   Point(-CELL_SIZE,0),
                   Point(0,CELL_SIZE),
                   Point(0, -CELL_SIZE)]
        self.delete_tree()
        self.delete_p()
        for point in offsets:
            self.position += point
            self.delete_tree()
            self.delete_p()
            self.position -= point

    def rotate_and_move(self, rotate):
            self.rotation = rotate
            self.move_forward(CELL_SIZE)
            if self.is_touching_any_sprite_with_tag("wall"):
                self.move_forward(-CELL_SIZE)
            if self.is_touching_any_sprite_with_tag("tree"):
                self.move_forward(-CELL_SIZE)

    def set_keys(self, up, down, left, right, bomb):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.bomb = bomb

    def on_update(self, dt):
        if window.is_key_down(self.up):
            self.rotate_and_move(90)
        if window.is_key_down(self.down):
            self.rotate_and_move(270)
        if window.is_key_down(self.left):
            self.rotate_and_move(180)
        if window.is_key_down(self.right):
            self.rotate_and_move(360)

        p = self.get_touching_sprites_with_tag("power_up")
        if p:
            p[0].delete()
            self.power += 1

        if window.is_key_down(self.bomb):
            b = window.create_sprite(Bomb)
            b.position = self.position
            b.power = self.power
            print(b.power)


        if self.is_touching_any_sprite_with_tag("explosion"):
            self.delete()
            window.close()

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
                window.create_sprite(PowerUp, x=x, y=y)

p1 = window.create_sprite(Player)
p1.set_keys(KeyCode.UP, KeyCode.DOWN, KeyCode.LEFT, KeyCode.RIGHT, KeyCode.SPACE)
p2 = window.create_sprite(Player)
p2.set_keys(KeyCode.W, KeyCode.S, KeyCode.A, KeyCode.D, KeyCode.ENTER)
p2.x += (WORLD_SIZE-3)*CELL_SIZE
p2.y += (WORLD_SIZE-3)*CELL_SIZE
p2.delete_neighboring_tree()

print(p1.power)

window.run()
