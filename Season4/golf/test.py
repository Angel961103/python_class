from math import sqrt
from pycat.core import Window, Sprite, Point, Color
from pycat.base.event import MouseEvent

w = Window()

class Ball(Sprite):
    def on_create(self):
        self.aim = w.create_line()
        self.scale = 0.1
        self.position = w.center
        self.image = "golfball.png"
        self.is_aimmimg = True

    def on_update(self, dt):
        if self.is_aimmimg == True:
            d = w.mouse_position - self.position
            if d.x == 0 and d.y == 0:
                self.aim.set_start_end(self.position, self.position)
            else:
                d.normalize()
                self.d = d
                self.aim.set_start_end(self.position, self.position+d*100)
        else:
            self.position += self.d*20

    def on_click_anywhere(self, mouse_event: MouseEvent):
        self.is_aimmimg = False
        


w.create_sprite(Ball)
w.run()