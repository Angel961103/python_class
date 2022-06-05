from posixpath import dirname
from pycat.core import Window, Sprite
from pycat.experimental.ldtk import LdtkFile
from level_entities import get_level_entities, List
from os.path import dirname

w = Window(is_sharp_pixel_scaling=True, enforce_window_limits=False)


class ScrollableLevel(Sprite):
    def on_create(self):
        self.speed = 10
        self.sprites: List[Sprite] = []
        self.layer = -1

    def create_entities(self, ldtk_file_path):
        data = get_level_entities(ldtk_file_path)
        for level in data:
            for e in level.entities:
                s = w.create_sprite(x=self.scale*e.x,
                                    y=self.scale*e.y,
                                    scale_x=self.scale*e.width,
                                    scale_y=self.scale*e.height,
                                    tags=e.tags,
                                    opacity=110)
                self.sprites.append(s)
                print(s)
            self.image = f'platformer_test/png/{level.id}.png'

    def update_entities_x(self, dx):
        for s in self.sprites:
            s.x += dx

    def on_update(self, dt):
        if w.is_key_pressed('a'):
            prev_x = self.x
            self.x += self.speed
            self.x = min(self.x, self.width/2)
            self.update_entities_x(self.x-prev_x)
        if w.is_key_pressed('d'):
            prev_x = self.x
            self.x -= self.speed
            self.x = max(self.x, w.width-self.width/2)
            self.update_entities_x(self.x-prev_x)


b = w.create_sprite(ScrollableLevel)
b.scale = 3

b.create_entities(dirname(__file__)+'/platformer_test.ldtk')
b.x = b.width/2
b.y = b.height/2
w.run()
