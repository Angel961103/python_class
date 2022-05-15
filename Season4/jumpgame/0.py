from pycat.core import Window, Color, Sprite
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller


window = Window(width=17*32, height=12*32)

ldtk_file = LdtkFile('jumping_levels2.ldtk')
ldtk_file.render_level(window, 'Level_0')


class Player(Sprite):
    def on_create(self):
        self.movement_controller = Controller(window, speed_factor=25)
        self.layer = 10
        self.scale = 30
        self.color = Color.ORANGE

    def on_update(self, dt):
        self.position += self.movement_controller.get_movement_delta(dt)


player = window.create_sprite(Player)

window.run()
