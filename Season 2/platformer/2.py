from enum import Enum, auto
from typing import List
from pycat.base.color import Color
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window ,Sprite

w = Window(background_image="Stars.png", width=960,height=720)

class PlayerState(Enum):
    WAIT = auto()
    MOVE = auto()
    RESET = auto()

class Player(Sprite):

    def on_create(self):
        self.image = "owl-a.png"
        self.reset()

    def reset (self):
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.position = (150,400)
        self.scale = 0.7
        self.state = PlayerState.MOVE

    def on_update(self, dt):
        if self.state == PlayerState.MOVE:
            self.y_speed -= 2
            self.x += self.x_speed
            self.y += self.y_speed
            if self.is_touching_window_edge():
                self.state = PlayerState.RESET
            for p in platforms:
                if self.is_touching_sprite(p.hitbox):
                    self.state = PlayerState.WAIT
                    self.y = p.hitbox.y + p.hitbox.height/2 + self.height/2
        if self.state == PlayerState.RESET:
            self.reset()

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == PlayerState.WAIT:
            x_jump = mouse_event.position.x - self.x
            y_jump = mouse_event.position.y - self.y
            self.x_speed = x_jump * 0.03
            self.y_speed = y_jump * 0.1
            self.state = PlayerState.MOVE

class Tree(Sprite):

    def on_create(self):
        self.scale = 1
        self.x = 100
        self.y = 200
    def add_hitbox(self):
        self.hitbox = w.create_sprite(position=self.position)
        self.hitbox.width = 100
        self.hitbox.height = 10
        self.hitbox.color = Color.RED

platforms: List[Tree]= [
    w.create_sprite(Tree, x=450, y=100, scale=0.7, image="tree1.png"),
    w.create_sprite(Tree, image="tree1.png"),
    w.create_sprite(Tree,x=800, y=280,scale = 1.5, image = "trees-a.png"),
]
for p in platforms:
    p.add_hitbox()

w.create_sprite(Player)


w.run()