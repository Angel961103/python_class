
from pycat.core import Window, Sprite, Color, KeyCode
from enum import Enum, auto

w = Window()
SPEED = 3

class Player(Sprite):
    def on_create(self):
        self.scale = 50
        self.color = Color.AMBER
        self.speed = 20
        
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed

class Enemy(Sprite):
    def on_create(self):
        self.scale = 50
        self.y = 100
        self.state = Enemy.State.WANDER
        self.target = w.create_sprite()
        self.target.scale = 20
        self.target.goto_random_position()
        self.outside_circle = w.create_arc(radius=400)
        self.inside_circle = w.create_arc(radius=200)
        self.label = w.create_label(text=str(self.state))
        self.label.position = self.position

    def on_update(self, dt):
        self.outside_circle.position = self.position.as_tuple()
        self.inside_circle.position = self.position.as_tuple()
        self.label.position = self.position
        self.label.text = str(self.state)
        if self.state is Enemy.State.WANDER:
            self.roam()
            if self.distance_to(player) < self.outside_circle._radius:
                self.state = Enemy.State.CHASE

        if self.state is Enemy.State.CHASE:
            self.point_toward_sprite(player)
            self.move_forward(SPEED)
            if self.distance_to(player) > self.outside_circle._radius:
                self.state = Enemy.State.WANDER
            if self.distance_to(player) < self.inside_circle._radius:
                self.state = Enemy.State.FIGHT

        if self.state is Enemy.State.FIGHT:
            self.point_toward_sprite(player)
            self.move_forward(SPEED)
            self.fight = w.create_sprite()
            self.fight.color = Color.RED
            self.fight.scale = 20
            self.fight.position = self.position.as_tuple()
            self.fight.point_toward_sprite(player)
            self.fight.move_forward(30)
            if self.fight.is_touching_any_sprite() or self.fight.is_touching_window_edge():
                self.fight.delete()
            if self.distance_to(player) < self.outside_circle._radius:
                self.state = Enemy.State.CHASE
            
            

    def roam(self):
        self.point_toward_sprite(self.target)
        self.move_forward(SPEED)
        if self.distance_to(self.target) < 20:
            self.target.goto_random_position()

    class State(Enum):

        WANDER = auto()
        CHASE = auto()
        FIGHT = auto()


              
player = w.create_sprite(Player)
w.create_sprite(Enemy)
w.run()