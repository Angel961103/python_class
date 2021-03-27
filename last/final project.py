from os import close
from typing import List
from pycat.core import Color, KeyCode, Sprite, Window, Label
import random
from pyglet.image import create

window = Window(draw_sprite_rects=True)

color_list: List['ColorSprite'] = []

class ColorSprite(Sprite):
    def on_create(self):
        self.scale =100
        self.speed = 10
        self.y = 300
        self.is_selected_color = False

    def on_update(self, dt):
        if self.is_selected_color:
            if window.get_key(KeyCode.W):
                self.y += self.speed
            if window.get_key(KeyCode.A):
                self.x-=self.speed
            if window.get_key(KeyCode.S):
                self.y -= self.speed
            if window.get_key(KeyCode.D):
                self.x+=self.speed

    def on_left_click(self):
        for c in color_list:
            c.is_selected_color = False
        self.is_selected_color = True

color_r = window.create_sprite(ColorSprite)
color_r.color = Color(255 ,0 ,0)
color_r.x = 100

color_g = window.create_sprite(ColorSprite)
color_g.color = Color(0 ,255 ,0)
color_g.x = 300

color_b = window.create_sprite(ColorSprite)
color_b.color = Color(0 ,0 ,255)
color_b.x = 500

color_bl = window.create_sprite(ColorSprite)
color_bl.color = Color(0 ,0 ,0)
color_bl.x = 700

color_list = [color_r, color_g, color_b, color_bl]

class Brush(Sprite):
    def on_create(self):
        self.color = Color.BLACK
        self.scale = 50

    def on_update(self, dt):
        self.position = window.mouse_position
        if self.touching_sprite(color_r):
            self.color = color_r.color
        if self.touching_sprite(color_g):
            self.color = color_g.color
        if self.touching_sprite(color_b):
            self.color = color_b.color
        if self.touching_sprite(color_bl):
             self.color = color_bl.color

brush = window.create_sprite(Brush)
class Task(Sprite):
    def on_create(self):
        self.x = 1080
        self.y = 100
        self.scale = 200
        self.create_color()

    def create_color(self):
        c1 = random.choice(color_list)
        c2 = random.choice(color_list)
        while c2.color.r == c1.color.r:
            c2 = random.choice(color_list)
        r,g,b = c1.color
        r += c2.color.r
        g += c2.color.g
        b += c2.color.b
        self.color = Color(r/2, g/2, b/2)

task = window.create_sprite(Task)
class  Player(Sprite):
    def on_create(self):
        self.x = 880
        self.y = 100
        self.scale = 100
        self.color = Color.BLACK

    def on_update(self, dt):
        if window.get_key_up(KeyCode.SPACE):
            self.color = Color.BLACK

        if window.get_key_up(KeyCode.ENTER) and self.color == task.color:
            print(self.color)
            task.create_color()
            self.color = Color(0 ,0 ,0)

    def on_left_click(self):
        if self.touching_sprite(brush):
            
            if self.color == Color.BLACK:
                self.color = brush.color
            else:
                r,g,b = self.color
                r += brush.color.r
                g += brush.color.g
                b += brush.color.b
                self.color = Color(r/2, g/2, b/2)


player = window.create_sprite(Player)

window.run()