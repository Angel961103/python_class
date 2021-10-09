from pycat.window import Window
from pycat.keyboard import KeyCode
from pycat.sprite import Sprite
from pycat.collision import is_aabb_collision
from pycat.scheduler import Scheduler
import random

from pyglet.image import create

w=Window(background_image="beach_03.png")
class Cat(Sprite):

    def on_create(self):
        self.image="cat.png"
        self.x=30
        self.y=30

    def on_update(self, dt):
        if w.get_key(KeyCode.LEFT):
            self.x=self.x-10
        if w.get_key(KeyCode.RIGHT):
            self.x=self.x+10

cat = w.create_sprite(Cat)

class Gem(Sprite):

    def on_create(self):
        self.image="gem_shiny01.png"
        self.goto_random_position()
        self.y=w.height
        self.scale=0.25

    def on_update(self, dt):
        self.y=self.y-7
        if self.y<0:
            self.delete()
        #if self.touching_any_sprite():
          #  self.delete()
        if is_aabb_collision(self,cat):
            self.delete()

filelist=["gem_shiny01.png","gem_shiny02.png","gem_shiny03.png","gem_shiny04.png","gem_shiny05.png"]

def create_gem(dt):
    w.create_sprite(Gem).image=random.choice(filelist)


Scheduler.update(create_gem, delay=1)




w.run()