from matplotlib import animation
from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator

w = Window(is_sharp_pixel_scaling=True)

def get_animation_dictionary(names, frames, directory):
    images = [
            [directory+names[i] + str(j+1) + ".png" 
            for j in range(frames[i])]
            for i in range(len(names))
             ]
    return {names[i]: images[i] for i in range(len(names))}

class Cat(Sprite):
    def on_create(self):
        self.names = ["jump", "paw", "look", "lick", "lickb", 
                      "scared", "run", "sit", "sleep", "sprint"]
        frames = [7, 6, 4, 4, 4, 8, 8, 4, 4, 8]
        directory = "cat/"
        animation_dict = get_animation_dictionary(self.names, frames, directory)
        self.animator = Animator(animation_dict)
        self.animator.play("jump")
        self.image = self.animator.tick(0)
        self.position = w.center
        self.scale = 10

    def on_update(self, dt):
        self.image = self.animator.tick(dt)

        for i in range(min(len(self.names), 10)):
            if w.is_key_down(ord(str(i))):
                self.animator.play(self.names[i])

w.create_sprite(Cat)
w.run()