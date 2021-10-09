from enum import Enum
from random import random
from threading import current_thread
from pycat.core import Window, Label, Sprite, Color, Scheduler
import random, os
from get_word import get_words

w = Window(enforce_window_limits=False)
file_1 = os.path.dirname(__file__) + "/n.txt"
file_2 = os.path.dirname(__file__) + "/v.txt"
file_3 = os.path.dirname(__file__) + "/adj.txt"

n = get_words(file_1)
adj = get_words(file_2)
v = get_words(file_3)
all = n + adj + v

class State(Enum):
    N = 0
    V = 1
    ADJ = 2
states = [State.N, State.V ,State.ADJ]
current_state = random.choice(states)
state_label = w.create_label()

class Word(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.label = w.create_label()

    def setup(self, x, y, t):
        self.x = x
        self.y = y
        self.label.text = t
        self.width = self.label.content_width
        self.height = self.label.content_height
        self.label.y = self.y + self.height/2
        self.label.x= self.x - self.width/2

    def on_update(self, dt):
        self.y -= 3
        self.label.y -= 3
        if self.y < 0:
            self.delete()
            self.label.delete()

    def good_click(self):
        score.current += 1
        score.check_high_score()

    def on_left_click(self):
        if self.label.text in n and states == State.N:
            self.good_click()
        elif self.label.text in v and states == State.V:
            self.good_click()
        elif self.label.text in adj and states == State.ADJ:
            self.good_click()
        self.delete()
        self.label.delete()

class Score(Label):

    def on_create(self):
        self.y = w.height
        self.x = w.width/2
        self.current = 0
        self.highscore = int(self.read_high_score())
        self.text = "High Score:" + self.read_high_score()

    def read_high_score(self):
        file_4 = os.path.dirname(__file__) + "/score.txt"
        return str(get_words(file_4)[0])




def work1(dt):
    word = w.create_sprite(Word)
    word.setup(random.randint(0, w.width), w.height, random.choice(all))

Scheduler.update(work1, delay=1)

def change_state(dt):
    global current_state
    current_state = random.choice(states)
    state_label.text = str(current_state)

Scheduler.update(change_state, delay=10)

score = w.create_label(Score)
w.run()