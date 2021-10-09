from pycat.base.color import Color
from pycat.core import Window, Point, Sprite
from math import sqrt

w = Window()

point_a = Point(100, 200)
point_b = Point(300, 200)
c = abs(point_a.x - point_b.x)
a = c/2
b = sqrt(c**2-a**2)
point_c = (point_a + point_b)/2
point_c.y += b

class MySprite(Sprite):

    def on_create(self):
        pass

    def draw_triangle(self, i):

        a = self.position
        self.move_forward(i)
        b = self.position
        self.rotation += 120
        self.move_forward(i)
        c = self.position
        w.create_line(a.x ,a.y, b.x, b.y, 1, Color.AMBER)
        w.create_line(b.x ,b.y, c.x, c.y, 1, Color.AZURE)
        w.create_line(c.x ,c.y, a.x, a.y, 1, Color.CHARTREUSE)

mys = w.create_sprite(MySprite)
mys.position = w.center
for i in range(100):
    mys.draw_triangle(i*4)
    mys.rotation += 5800


w.run()