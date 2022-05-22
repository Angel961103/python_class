from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator
from pycat.experimental.spritesheet import SpriteSheet

w = Window(is_sharp_pixel_scaling=True)

def get_animation_dictionary(names, frames, directory):
    images = [
            [directory+names[i] + str(j+1) + ".png" 
            for j in range(frames[i])]
            for i in range(len(names))
             ]
    return {names[i]: images[i] for i in range(len(names))}

class Wizard(Sprite):
    def on_create(self):
        self.names = ["attack"]
        sheet = SpriteSheet("wizard/Attack1.png", 231, 190)
        self.textures = [sheet.get_texture(i, 0) for i in range(8)]
        
        animation_dict = {self.names[0]: self.textures}
        self.animator = Animator(animation_dict)
        self.animator.play(self.names[0])
        self.texture = self.animator.tick(0)
        self.position = w.center
        self.scale = 1

    def on_update(self, dt):
        self.texture = self.animator.tick(dt)

w.create_sprite(Wizard)
w.run()