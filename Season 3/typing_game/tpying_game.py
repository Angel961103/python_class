from pycat.base.color import Color
from pycat.core import Window, Label
from pycat.base.event import KeyEvent
from pycat.sprite import Sprite
from random import choice

w = Window()

word_list = ["random", "is", "not", "island", "orange", "rabbit"]

class TypingLabel(Label):
    def on_create(self):
        self.text = choice(word_list)
        # self.current = 0
        self.font_size = 20

    def is_current(self, c:str) -> bool:
        if self.text[0] == c:
            self.text = self.text[1:]
            # self.current += 1
            if 0 == len(self.text):
                self.text = choice(word_list)
                # self.current = 0
            return True
        else:
            return False

class Player(Sprite):
    def on_create(self):
        self.scale = 150
        self.x = 100
        self.y = 100
        self.color = Color.AMBER
        self.add_tag("player")
        self.label = w.create_label(text="0", x=self.x, y=self.y)

class Enemy(Sprite):

    speed = 1
    def on_create(self):
        self.scale = 250
        self.x = 700
        self.y = 100
        self.color = Color.CHARTREUSE
        self.add_tag("enemy")

    def on_update(self, dt):
        global enemy
        if self.is_touching_any_sprite_with_tag("player"):
            print("you lose")
            self.delete()
            enemy = w.create_sprite(Enemy)
        if self.is_touching_window_edge():
            print("you win")
            self.delete()
            player.label.text = str(1 + int(player.label.text))
            enemy = w.create_sprite(Enemy)
            Enemy.speed *= 2
        self.x -= Enemy.speed

class Projectile(Sprite):
    def on_create(self):
        self.scale = 20
        self.color = Color.AZURE
        self.goto(player)
        self.add_tag("projectile")
        
    def on_update(self, dt):
        self.x += 10
        if self.is_touching_any_sprite_with_tag("enemy"):
            enemy.x += 50
            self.delete()
        if self.is_touching_window_edge():
            self.delete()

def key_press(key: KeyEvent):
    if label.is_current(key.character):
        p = w.create_sprite(Projectile)
        
        

player = w.create_sprite(Player)
w.subscribe(on_key_press=key_press)
label = w.create_label(TypingLabel)
enemy = w.create_sprite(Enemy)
w.run()