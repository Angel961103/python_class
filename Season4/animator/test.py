from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator

w = Window(is_sharp_pixel_scaling=True)

class Cat(Sprite):
    def on_create(self):
        self.animator = Animator()

        image_list = ["cat/jump" + str(i+1) + ".png"
                      for i in range(7)]
        self.animator.add("jump", image_list)
        self.animator.play("jump")

        image_list = ["cat/scared" + str(i+1) + ".png"
                      for i in range(8)]
        self.animator.add("scared", image_list)
        self.animator.play("scared")

        self.image = self.animator.tick(0)
        self.position = w.center
        self.scale = 10

    def on_update(self, dt):
        self.image = self.animator.tick(dt)

        if w.is_key_down(KeyCode.J):
            self.animator.play("jump")
        
        if w.is_key_down(KeyCode.S):
            self.animator.play("scared")

w.create_sprite(Cat)
w.run()