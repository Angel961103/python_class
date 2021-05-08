from pycat.base import color
from pycat.core import Window, Sprite, Color

GAP = 10
WIDTH = 500
HEIGHT = 700
BUTTON = 5
NEW_WIDTH = WIDTH - 6*GAP
BUTTON_WIDTH = NEW_WIDTH/5

w = Window(width=WIDTH, height=HEIGHT)

code_list = []
guess_list = []

class Colorsprite(Sprite):
    current_color = None

    def on_create(self):
        self.width = BUTTON_WIDTH
        self.height = BUTTON_WIDTH
        self.x = GAP + BUTTON_WIDTH/2
        self.y = GAP + BUTTON_WIDTH/2

    def on_left_click(self):
        Colorsprite.current_color = self.color

class Colorcode(Sprite):

    def on_create(self):
        self.width = BUTTON_WIDTH
        self.height = BUTTON_WIDTH
        self.x = GAP + BUTTON_WIDTH/2
        self.y = HEIGHT - (GAP + BUTTON_WIDTH/2)

class Colorguess(Sprite):
    current_guess = 1
    def on_create(self):
        self.width = BUTTON_WIDTH
        self.height = BUTTON_WIDTH
        self.x = GAP + BUTTON_WIDTH/2
        self.y = 2*GAP + BUTTON_WIDTH*1.5

    def on_left_click(self):
        if Colorsprite.current_color:
            self.color = Colorsprite.current_color

class Check(Sprite):

    def on_create(self):
        self.width = BUTTON_WIDTH
        self.height = BUTTON_WIDTH
        self.x = WIDTH - (GAP+BUTTON_WIDTH/2)
        self.y = GAP + BUTTON_WIDTH/2
        self.current_guess = 0

    def on_left_click(self):
        v = check_red_score()
        draw_red_peg(v,self.current_guess)
        if guess_equals_code():
            print("you win")
        else:
            print("try again")
            self.current_guess += 1
            make_new_guess(self.current_guess)

def guess_equals_code():
    for i in range(len(guess_list)):
        g = guess_list[i].color
        c = code_list[i].color
        if g != c:
            return False
    return True

def make_new_guess(guess):
    guess_list.clear()
    for k in range(BUTTON-1):
        c = w.create_sprite(Colorguess)
        c.color = Color.WHITE
        c.x += k*(GAP + BUTTON_WIDTH)
        c.y += guess*(GAP + BUTTON_WIDTH)
        guess_list.append(c)

def check_red_score():
    red_right = 0
    for i in range(len(guess_list)):
        g = guess_list[i].color
        c = code_list[i].color
        if g == c:
            red_right += 1
    return red_right

def draw_red_peg(v,guess):
    for i in range(v):
        s = w.create_sprite(Score)
        s.color = Color.RED
        s.x -= i*(s.scale + 5)
        s.y += guess*(GAP + BUTTON_WIDTH)

c_list = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]

class Score(Sprite):

    def on_create(self):
        self.scale = BUTTON_WIDTH/5
        self.x = WIDTH - self.scale
        self.y = 2*GAP + BUTTON_WIDTH*1.5

    def on_update(self, dt):
        pass

for i in range(len(c_list)):
    c = w.create_sprite(Colorsprite)
    c.color = c_list[i]
    c.x += i*(GAP + BUTTON_WIDTH)

for j in range(len(c_list)):
    c = w.create_sprite(Colorcode)
    c.color = choice(c_list)
    c.x += j*(GAP + BUTTON_WIDTH)
    code_list.append(c)

for k in range(len(c_list)):
    c = w.create_sprite(Colorguess)
    c.color = Color.WHITE
    c.x += k*(GAP + BUTTON_WIDTH)
    guess_list.append(c)

w.create_sprite(Check)
w.run()