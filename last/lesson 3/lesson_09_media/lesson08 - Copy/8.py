from inspect import classify_class_attrs
from pycat.window import Window
from pycat.sprite import Sprite
import random
from pycat.core import Player, AudioLoop

hit=Player("hit.wav")
laugh=Player("laugh.wav")
point=Player("point.wav")
audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
w=Window(background_image="forest_04.png",draw_sprite_rects=True)

check_sprite=[]
card=4*["avatar_01.png","avatar_02.png","avatar_03.png","avatar_04.png"]

class Card (Sprite):

    def on_create(self):
        self.is_visible=False
        self.is_rotation=False

    def on_update(self,dt):
        if self.is_rotation:
            self.rotation+=1
            self.scale-=0.01
        if self.rotation==40:
            self.color=200,0,0
        if self.rotation==100:
            self.delete()

    def on_left_click(self):
        if self not in check_sprite:
            if len(check_sprite)<2:
                hit.play()
                self.is_visible=True
                check_sprite.append(self)

class Button (Sprite):

    def on_create(self):
        self.image="button.png"
        self.scale=0.5
        self.x=600
        self.y=300
    def on_left_click(self):
        if len (check_sprite)==2:
            s1:Card=check_sprite[0]
            s2:Card=check_sprite[1]
            if s1.image==s2.image:
                s1.is_rotation=True
                s2.is_rotation=True
                point.play()
            else:
                laugh.play()
                s1.is_visible=False
                s2.is_visible=False
            check_sprite.clear()



random.shuffle(card)
for x in range(100,500,100):
    for y in range(100,500,100):
        w.create_sprite(Card, x=x, y=y,image=card.pop())

w.create_sprite(Button)
audio_loop.play()
w.run()