from pycat.collision import is_buffered_aabb_collision, is_buffered_rotated_box_collision
from pycat.window import Window
from pycat.sprite import Sprite
from pycat.scheduler import Scheduler
from pyglet.image import SolidColorImagePattern

w=Window(background_image="underwater_04.png")


class UFO (Sprite):

    def on_create(self):
        self.image="saucer.png"
        self.y=500
        self.scale=0.3
        self.score=0
        self.add_tag("spaceship")

    def on_update(self, dt):
        self.move_forward(10)
        if self.touching_window_edge():
            self.rotation+=180


ufo = w.create_sprite(UFO)


class Alien(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.image="1.png"
        self.scale=0.25
        self.y=50
        self.is_moving_up=False
        
    def on_update(self, dt):
        if self.is_moving_up==True:
            self.y+=20
        if self.touching_any_sprite_with_tag("spaceship"):
            ufo.score+=1
            print(ufo.score)
            self.delete()
            
        if self.touching_window_edge():
            self.delete()


    def on_left_click(self):
        self.is_moving_up=True

def create_alien(dt):
    w.create_sprite(Alien)

Scheduler.update(create_alien,1)


w.create_sprite(Alien)
w.run()