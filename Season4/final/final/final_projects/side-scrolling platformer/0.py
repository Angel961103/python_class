from pycat.core import Window, Sprite

w = Window(is_sharp_pixel_scaling=True, enforce_window_limits=False)


class ScrollableBackground(Sprite):
    def on_create(self):
        self.image = 'platformer_test/png/Level_0.png'
        self.speed = 50

    def on_update(self, dt):
        if w.is_key_pressed('a'):
            self.x += self.speed
            self.x = min(self.x, self.width/2)
        if w.is_key_pressed('d'):
            self.x -= self.speed
            self.x = max(self.x, w.width-self.width/2)


b = w.create_sprite(ScrollableBackground)
b.scale = 3.1
b.x = b.width/2
b.y = b.height/2
w.run()
