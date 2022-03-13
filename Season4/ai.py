
from asyncore import compact_traceback
from pycat.core import Window, Sprite, Color, KeyCode
from enum import Enum, auto

from pytest import Item

w = Window()
SPEED = 2
PLAYER_SPEED = 10

class Player(Sprite):
    def on_create(self):
        self.scale = 50
        self.color = Color.AMBER
        self.speed = PLAYER_SPEED
        
    def on_update(self, dt):
        if self.is_touching_sprite(item):
            self.speed += 0.1

        # if self.is_touching_sprite(enemy):
        #     self.speed -= 0.1
        #     if self.speed <= 1:
        #         w.close()

        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed

class Item(Sprite):
    def on_create(self):
        self.scale = 20
        self.color = Color.ORANGE
        self.goto_random_position()

    def on_update(self, dt):
        if self.is_touching_sprite(player):
            self.goto_random_position()

class Enemy(Sprite):
    def on_create(self):
        self.scale = 50
        self.y = 100
        self.state = Enemy.State.WANDER
        self.target = w.create_sprite()
        self.target.color = Color.GREEN
        self.target.scale = 20
        self.target.goto_random_position()
        self.outside_circle = w.create_arc(radius=400)
        self.middle_circle = w.create_arc(radius=250)
        self.inside_circle = w.create_arc(radius=100)
        self.label = w.create_label(text=str(self.state))
        self.label.position = self.position

    def set_weapon(self, weapon):
        self.weapon: Sprite = weapon

    def on_update(self, dt):
        self.circle_position()

        if self.state is Enemy.State.WANDER:
            self.roam()
            if self.distance_to(player) < self.outside_circle._radius:
                self.state = Enemy.State.WARN

        if self.state is Enemy.State.WARN:
            self.warn()
            if self.distance_to(player) < self.middle_circle._radius:
                self.state = Enemy.State.CHASE
                self.weapon.is_visible = True
            if self.distance_to(player) > self.outside_circle._radius:
                self.state = Enemy.State.WANDER
                self.weapon.is_visible = False

        if self.state is Enemy.State.CHASE:
            self.chase()
            if self.distance_to(player) > self.middle_circle._radius:
                self.state = Enemy.State.WARN
                self.weapon.is_visible = False
            if self.distance_to(player) < self.inside_circle._radius:
                self.state = Enemy.State.FIGHT

        if self.state is Enemy.State.FIGHT:
            self.fight()
            if self.distance_to(player) > self.inside_circle._radius:
                self.state = Enemy.State.CHASE

    def circle_position(self):
        self.outside_circle.position = self.position.as_tuple()
        self.middle_circle.position = self.position.as_tuple()
        self.inside_circle.position = self.position.as_tuple()
        self.label.position = self.position
        self.label.text = str(self.state)

    def roam(self):
        self.point_toward_sprite(self.target)
        self.move_forward(SPEED-1)
        if self.distance_to(self.target) < 20:
            self.target.goto_random_position()

    def warn(self):
        self.point_toward_sprite(player)
        self.move_forward(SPEED+1)

    def chase(self):
        self.point_toward_sprite(player)
        self.move_forward(SPEED+3)
        # self.weapon.position = self.position
        # self.weapon.point_toward_sprite(player)
        # self.weapon.move_forward(self.width/2 +self.fight_sprite.width/2)

    def fight(self):
        self.point_toward_sprite(player)
        self.move_forward(SPEED)

    class State(Enum):
        WANDER = auto()
        WARN = auto()
        CHASE = auto()
        FIGHT = auto()


class Boomerang(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.scale = 20
        self.speed = 30
        self.is_visible = False
        self.state = Boomerang.State.HOLDING
        self.enemy = enemy

    def on_update(self, dt):
        if self.state is Boomerang.State.HOLDING:
            self.goto(self.enemy)

    class State(Enum):
        HOLDING = auto()
        THROW_FOWARD = auto()
        COME_BACK = auto()


player = w.create_sprite(Player)
item = w.create_sprite(Item)
enemy = w.create_sprite(Enemy)
boomerang = w.create_sprite(Boomerang)
enemy.set_weapon(boomerang)
w.run()