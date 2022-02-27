from math import sqrt
from pycat.core import Window, Sprite, Point, Color
from pycat.base.event import MouseEvent

w = Window()
w.set_clear_color(126, 200, 80)
hole = w.create_circle(700, 500, 30, Color.BLACK)
SPEED = 0.05
FRICTION = 0.97

def dot(u: Point, v: Point):
    return u.x * v.x + u.y * v.y

def project(u: Point, v: Point):
    return dot(u, v) * v / dot(v, v)

def reflect(u: Point, v: Point):
    return u - 2 * project(u, v)


class Ball(Sprite):
    def on_create(self):
        self.aim = w.create_line()
        self.scale = 0.1
        self.image = "golfball.png"
        self.is_aimmimg = True
        self.speed = 0

    def on_update(self, dt):
        if self.is_aimmimg:
            self.set_is_aiming(True)
        else:
            self.position += self.speed
            self.speed *= FRICTION
            d = (self.position - Point(hole.x, hole.y)).magnitude()
            if d < hole.radius:
                w.close()
            
            self.bounce()
            if self.speed.magnitude() <= 1:
                self.set_is_aiming(True)

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.is_aimmimg:
            self.set_is_aiming(False)

    def set_is_aiming(self, b):
        dp = w.mouse_position - self.position
        self.speed = SPEED * dp
        self.is_aimmimg = b
        self.aim.visible = b
        if dp.x == 0 and dp.y == 0:
            self.aim.set_start_end(self.position, self.position)
        else:
            dp.normalize()
            self.aim.set_start_end(self.position, self.position+dp*100)

    def bounce(self):
        walls = self.get_touching_sprites_with_tag("wall")
        if walls:
            self.speed = reflect(self.speed, walls[0].n)
            
class Wall(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale_x = 50
        self.scale_y = 250
        self.add_tag("wall")

    def normal(self):
        p1 = self.position
        self.move_forward(1)
        p2 = self.position
        self.move_forward(-1)
        self.n = p2 - p1
        p3 = p1 + 100*self.n
        w.create_line(p1.x, p1.y, p3.x, p3.y, 5)

def create_wall(x, y, rot):
    wall = w.create_sprite(Wall, x=x, y=y, rotation=rot)
    wall.normal()


create_wall(400, 500, 0)
create_wall(500, 100, 90)
create_wall(800, 500, 180)
create_wall(1000, 200, -220)
create_wall(200, 100, 200)
create_wall(200, 600, 270)
w.create_sprite(Ball)
w.run()