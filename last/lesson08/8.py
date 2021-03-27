from inspect import classify_class_attrs
from pycat.window import Window
from pycat.sprite import Sprite
from random import randrange

w=Window(background_image="forest_04.png",draw_sprite_rects=True)

check_sprite=[]
card=["avatar_01.png","avatar_02.png","avatar_03.png","avatar_04.png"]

class Card (Sprite):

    def on_create(self):
        self.is_visible=False
    
    def on_left_click(self):
        if self not in check_sprite:
            if len(check_sprite)<2:
                self.is_visible=True
                check_sprite.append(self)

r=randrange(0,3)
r1=randrange(0,3)
r2=randrange(0,3)
r3=randrange(0,3)
r4=randrange(0,3)
r5=randrange(0,3)
r6=randrange(0,3)
r7=randrange(0,3)
r8=randrange(0,3)
r9=randrange(0,3)

class Button (Sprite):

    def on_create(self):
        self.image="button.png"
        self.scale=0.5
        self.x=500
        self.y=200
    def on_left_click(self):
        if len (check_sprite)==2:
            s1:Sprite=check_sprite[0]
            s2:Sprite=check_sprite[1]
            if s1.image==s2.image:
                s1.delete()
                s2.delete()
            else:
                s1.is_visible=False
                s2.is_visible=False
            check_sprite.clear()

        print (check_sprite)


w.create_sprite(Card, x=100, y=100, image=card[r])
w.create_sprite(Card, x=100, y=200, image=card[r1])
w.create_sprite(Card, x=200, y=100, image=card[r2])
w.create_sprite(Card, x=200, y=200, image=card[r3])
w.create_sprite(Card, x=300, y=200, image=card[r4])
w.create_sprite(Card, x=300, y=100, image=card[r5])
w.create_sprite(Card, x=300, y=300, image=card[r6])
w.create_sprite(Card, x=200, y=300, image=card[r7])
w.create_sprite(Card, x=100, y=300, image=card[r8])
w.create_sprite(Card, x=400, y=100, image=card[r9])

w.create_sprite(Button)
w.run()