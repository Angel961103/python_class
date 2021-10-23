from pycat.base.color import Color
from pycat.base.event.key_event import KeyCode
from pycat.core import Window, Sprite

CELL_SIZE = 50

w = Window()

level = ["wwwwwwwwwwww",
         "w r   w    w",
         "w   p   b  w",
         "w   r   w  w",
         "w  w b  w  w",
         "w          w",
         "wwwwwwwwwwww"]

rows = len(level)
cols = len(level[0])

class Player(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE
        self.x = 300
        self.y = 400
        self.add_tag("player")

    def on_update(self, dt):
        if w.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
            self.move_forward(CELL_SIZE)
        if w.is_key_down(KeyCode.LEFT):
            self.rotation = 180
            self.move_forward(CELL_SIZE)
        if w.is_key_down(KeyCode.UP):
            self.rotation = 90
            self.move_forward(CELL_SIZE)
        if w.is_key_down(KeyCode.DOWN):
            self.rotation = -90
            self.move_forward(CELL_SIZE)
        if self.is_touching_any_sprite_with_tag("wall"):
            self.move_forward(-CELL_SIZE)

class Box(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-2
        self.color = Color.RED
        self.add_tag("box")
        self.layer = 5

    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            self.rotation = player.rotation
            self.move_forward(CELL_SIZE)
        if self.is_touching_any_sprite_with_tag("wall"):
            self.move_forward(-CELL_SIZE)
            player.move_forward(-CELL_SIZE)
        if self.is_touching_any_sprite_with_tag("box"):
            self.move_forward(-CELL_SIZE)
            player.move_forward(-CELL_SIZE)
        if self.is_touching_any_sprite_with_tag("target"):
            targets = w.get_sprites_with_tag("target")
            count = 0
            for t in targets:
                if t.is_touching_any_sprite_with_tag("box"):
                    count += 1
            if count == len(targets):
                w.close()

class Target(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-10
        self.color = Color.GREEN
        self.add_tag("target")

class Wall(Sprite):
    def on_create(self):
        self.scale = CELL_SIZE-1
        self.color = Color.BLUE
        self.add_tag("wall")

def make_wall(x, y, width):
    for i in range(width):
        wall = w.create_sprite(Wall)
        wall.x = x + i*CELL_SIZE
        wall.y = y

def make_box(x, y):
    box = w.create_sprite(Box)
    box.x = x
    box.y = y

def make_target(x, y):
    target = w.create_sprite(Target)
    target.x = x
    target.y = y

# make_wall(100, 300, 20)
# make_wall(100, 500, 20)
# make_box(600, 400)
# make_box(400, 400)
# make_target(100, 400)
# make_target(800, 400)
x0 = 100
y0 = 500

for i in range(rows):
    for j in range(cols):
        if level[i][j] == "w":
            make_wall(x0+j*CELL_SIZE, y0-i*CELL_SIZE, 1)
        elif level[i][j] == "b":
            make_box(x0+j*CELL_SIZE, y0-i*CELL_SIZE)
        elif level[i][j] == "r":
            make_target(x0+j*CELL_SIZE, y0-i*CELL_SIZE)
        elif level[i][j] == "p":
            player = w.create_sprite(Player)

w.run()