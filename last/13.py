from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
import random

window = Window()

class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10
        self.add_tag("player")

    def on_update(self, dt):
        if window.get_key(KeyCode.W):
            self.y += self.speed
        if window.get_key(KeyCode.A):
            self.x-=self.speed
        if window.get_key(KeyCode.S):
            self.y -= self.speed
        if window.get_key(KeyCode.D):
            self.x+=self.speed
    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)

player = window.create_sprite(Player)

class Bullet(Sprite):
    def on_create(self):
        self.color = Color.BLUE
        self.scale = 15
        self.speed = 15
        self.position = player.position
        self.add_tag("Bullet")

    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()

class Enemy (Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 30
        self.speed = 5
        self.x = random.randint(0,360)
        self.y = random.randint(0,360)
        self.rotation = random.randint(0,90)
        self.time = 0
        self.add_tag("enemy")

    def on_update(self, dt):
        if self.time > 70:
            self.time = 0
            b = window.create_sprite(Enemy_Bullet)
            b.position = self.position
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('Bullet'):
            self.delete()
        self.time += 1


def spawn_enemy(dt):
    window.create_sprite(Enemy)

Scheduler.update(spawn_enemy, delay=2)

class Enemy_Bullet(Sprite):
    def on_create(self):
        self.color = Color.VIOLET
        self.scale = 15
        self.speed = 10
        self.add_tag("Enemy_Bullet")

    def on_update(self, dt):
        self.point_toward_sprite(player)
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag("player"):
            self.delete()


player = window.create_sprite(Player)
window.run()