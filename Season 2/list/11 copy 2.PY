from pycat.core import Sprite, Color, Window

PIXEL = 50

color = {
    "p":Color.PURPLE,
    "w":Color.WHITE,
    "b":Color.BLUE,
    "a":Color.AZURE,
    "c":Color.AMBER,
    "d":Color.BLACK,
    
}

my_list = [
    "wwwwwww",
    "ppppppp",
    "pbpppbp",
    "ppppppp",
    "ppwwwpp",
]

current_color = Color.WHITE

w = Window(width=len(my_list[0])*PIXEL+100, height=len(my_list)*PIXEL)

class Pixel(Sprite):
    def on_create(self):
        self.scale = PIXEL

class ColorChoice(Sprite):
    def on_create(self):
        self.scale = PIXEL
    def on_left_click(self):
        global current_color
        current_color = self.color

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        p = w.create_sprite(Pixel)
        p.x = j*(p.width+1) + p.width/2
        p.y = w.height - p.height/2 - i*(p.height+1)
        p.color = color[my_list[i][j]]

for k in range(2):
    pass
c = w.create_sprite(ColorChoice)
w.run()