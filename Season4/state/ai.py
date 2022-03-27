from pycat.core import Window, Sprite, Color, KeyCode
from enum import Enum, auto
from time import sleep

w = Window()
SPEED = 2
PLAYER_SPEED = 9

class Player(Sprite):
    def on_create(self):
        self.scale = 50
        self.color = Color.AMBER
        self.speed = float(PLAYER_SPEED)
        
        
    def on_update(self, dt):
        if self.is_touching_sprite(boomerang):
            self.speed -= 0.1
            if self.speed <= 0:
                sleep(2)
                w.close()

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
        self.label = w.create_label(text=str(round(player.speed, 3)))

    def on_update(self, dt):
        if self.is_touching_sprite(player):
            player.speed += 0.1
            self.label.text = str(round(player.speed, 3))
            print(player.speed)
            self.goto_random_position()

class Enemy(Sprite):
    def on_create(self):
        self.scale = 50
        self.y = 500
        self.x = 600
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
        self.weapon = None
        self.hand = w.create_sprite(scale = 2)
        self.hand.opacity = 0

    def set_weapon(self, weapon: "Boomerang"):
        self.weapon = weapon
        weapon.owner = self

    def on_update(self, dt):
        self.circle_position()
        self.hand.goto(self)
        if self.state is Enemy.State.WANDER:
            self.roam()
            if self.distance_to(player) < self.outside_circle._radius:
                self.state = Enemy.State.WARN

        if self.state is Enemy.State.WARN:
            self.warn()
            if self.distance_to(player) < self.middle_circle._radius:
                self.state = Enemy.State.CHASE
                self.weapon.is_visible = True
                if self.weapon.state is Boomerang.State.HOLDING:
                    self.weapon.attack(player)
            if self.distance_to(player) > self.outside_circle._radius:
                self.state = Enemy.State.WANDER

        if self.state is Enemy.State.CHASE:
            self.chase()
            if self.distance_to(player) > self.middle_circle._radius:
                self.state = Enemy.State.WARN
            if self.distance_to(player) < self.inside_circle._radius:
                self.state = Enemy.State.FIGHT

        if self.state is Enemy.State.FIGHT:
            self.fight()
            if self.distance_to(player) > self.inside_circle._radius:
                self.state = Enemy.State.CHASE
                if self.weapon.state is Boomerang.State.HOLDING:
                    self.weapon.attack(player)

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

    def fight(self):
        self.point_toward_sprite(player)
        self.move_forward(SPEED+2)

    class State(Enum):
        WANDER = auto()
        WARN = auto()
        CHASE = auto()
        FIGHT = auto()

class Boomerang(Sprite):
    def on_create(self):
        self.layer = 5
        self.color = Color.RED
        self.speed = 15
        self.state = Boomerang.State.HOLDING
        self.owner: Enemy = None
        self.throw_distance = 0
        self.max_d = 500
        self.target = None
        self.image = "b.png"
        self.scale_to_height(20)

    def on_update(self, dt):
        if self.state is Boomerang.State.HOLDING:
            self.goto(self.owner)
            if self.target:
                self.state = Boomerang.State.THROW_FOWARD
                self.point_toward_sprite(self.target)
                self.throw_distance = 0

        if self.state is Boomerang.State.THROW_FOWARD:
            self.move_forward(self.speed)
            self.throw_distance += self.speed
            self.image_rotation += 20
            self.image_rotation %= 360
            if self.throw_distance > self.max_d:
                self.state = Boomerang.State.COME_BACK
                self.target = None
            elif self.is_touching_sprite(self.target):
                self.state = Boomerang.State.COME_BACK
                self.target = None

        if self.state is Boomerang.State.COME_BACK:
            self.image_rotation += 20
            self.image_rotation %= 360
            self.point_toward_sprite(self.owner)
            self.move_forward(self.speed)
            if self.is_touching_sprite(self.owner.hand):
                self.state = Boomerang.State.HOLDING

    def attack(self, target):
        self.target = target

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