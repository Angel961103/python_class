from pycat.core import Window as W
from pycat.core import Sprite
from typing import List
from random import randint
w1 = W()

class Turtle(Sprite):
    def on_create(self):
        pass

    def forward(self, distance):
        x = self.x
        y = self.y
        self.move_forward(distance)
        w1.create_line(x,y,self.x,self.y)

    def draw_rect(self, w, h):
        self.forward(w)
        self.rotation += 90
        self.forward(h)
        self.rotation += 90
        self.forward(w)
        self.rotation += 90
        self.forward(h)
        self.rotation += 90

class Building():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        x = self.x + self.w/3
        x2 = self.x + 2*self.w/3
        y = self.y + self.h/2
        self.windows : List['Window'] = []
        for j in range(self.h//70):
            y = self.y + j*50 + 10
            self.windows.append(Window(x,y,30,30))
            self.windows.append(Window(x2,y,30,30))

    def draw(self, t:Turtle):
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.w, self.h)
        for w in self.windows:
            w.draw(t)

class Window():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self, t:Turtle):
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.w, self.h)

t = w1.create_sprite(Turtle)
for i in range(6):
    b = Building(i*200,0,190,randint(300,600))
    b.draw(t)

w1.run()