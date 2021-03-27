from pycat.core import Window ,Sprite ,KeyCode ,Scheduler ,Label
import random

w = Window(enforce_window_limits=False)

class Player(Sprite):
    def on_create(self):
        self.image = "bird.gif"
        self.x = 100
        self.y = w.height/2
        self.scale = 0.3

    def on_update(self, dt):
        self.y -= 2
        if w.is_key_down(KeyCode.SPACE):
            self.y += 40

class Pipe(Sprite):

    def on_create(self):
        self.image = "pipe.png"
        self.x = w.width + self.width/2

    def on_update(self, dt):
        self.x -= 2
        if self.x < -self.width/2:
            self.delete()

class Score(Label):
    def on_create(self):
        self.text = "Score:"

def make_pipe(dt):
    buttom_pipe = w.create_sprite(Pipe)
    top_pipe = w.create_sprite(Pipe)
    a = int(buttom_pipe.height/2)
    offset = random.randint(-a ,a)
    buttom_pipe.y += offset
    top_pipe.y = w.height + offset 
    top_pipe.rotation += 180

Scheduler.update(make_pipe ,5)
w.create_label(Score)
w.create_sprite(Player)
w.run()