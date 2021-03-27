from pycat.core import Sprite, Color, Window

PIXEL = 48

color = {
    "p":"tiles/tile_000.png",
    "w":"tiles/tile_001.png",
    "b":"tiles/tile_002.png",
}

my_list = [
    "wwwwwww",
    "ppppppp",
    "pbpppbp",
    "ppppppp",
    "ppwwwpp",
]
w = Window(width=len(my_list[0])*PIXEL, height=len(my_list)*PIXEL)
class Pixel(Sprite):

    def on_create(self):
        self.scale = 3

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        p = w.create_sprite(Pixel)
        
        p.image = color[my_list[i][j]]
        p.scale = 3
        p.x = j*(p.width+1) + p.width/2
        p.y = w.height - p.height/2 - i*(p.height+1)
        # if my_list[i][j] == "p":
        #     p.color = Color.PURPLE
        # if my_list[i][j] == "w":
        #     p.color = Color.WHITE

w.run()