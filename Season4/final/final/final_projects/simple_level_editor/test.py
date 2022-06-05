from pycat.core import Window, Sprite, Color
from make_platforms import generate_level as make_platforms
from make_ladders import generate_level as make_ladders
from enum import Enum, auto
from simple_level_editor import start_level_editor

w = Window(enforce_window_limits=False)
make_ladders(w, 'ladder')
w.get_sprite_with_tag('ladder').color = Color.CHARTREUSE
w.get_sprite_with_tag('ladder').layer = 1
make_platforms(w, 'platform')

# start_level_editor(w, 'make_more.py')


class Player(Sprite):
    GRAVITY = -0.9
    JUMP_VELOCITY = 15
    FRICTION = 0.9
    MAX_SPEED = 20
    ACCELERATION = 1.
    CLIMB_SPEED = 4

    class State(Enum):
        STANDING = auto()
        JUMPING = auto()
        FALLING = auto()
        CLIMBING = auto()

    def on_create(self):
        self.scale = 30
        self.position = w.center
        self.dy = 0
        self.dx = 0
        self.state = Player.State.FALLING
        self.color = (255, 0, 0)
        self.layer = 2

    def is_on_a_platform(self):
        if self.dy <= 0:
            ground = self.get_touching_sprites_with_tag('platform')
            if ground:
                min_y = ground[0].y + (self.height + ground[0].height)/2
                if self.y - self.dy >= min_y:
                    self.dy = 0
                    self.y = min_y
                    return True
        return False

    def is_on_a_ladder(self):
        return bool(self.get_touching_sprites_with_tag('ladder'))

    def is_on_top_of_ladder(self):
        ladders = self.get_touching_sprites_with_tag('ladder')
        return self.y > ladders[0].y if ladders else False

    def is_on_bottom_of_ladder(self):
        ladders = self.get_touching_sprites_with_tag('ladder')
        return self.y < ladders[0].y if ladders else False

    def on_update(self, dt):
        # All States
        self.dx *= self.FRICTION
        if abs(self.dx) < self.ACCELERATION*self.FRICTION:
            self.dx = 0
        self.y += self.dy
        self.x += self.dx
        self.x = min(self.x, w.width)
        self.x = max(0, self.x)
        if w.is_key_pressed('a'):
            self.dx -= self.ACCELERATION
            self.dx = max(self.dx, -self.MAX_SPEED)
        if w.is_key_pressed('d'):
            self.dx += self.ACCELERATION
            self.dx = min(self.dx, self.MAX_SPEED)

        # State Specific
        if self.state is self.State.FALLING:
            self.dy += self.GRAVITY
            if self.is_on_a_platform():
                self.state = self.State.STANDING

        elif self.state is self.State.JUMPING:
            self.dy += self.GRAVITY
            if self.is_on_a_platform():
                self.state = self.State.STANDING
            else:
                if w.is_key_pressed('w'):
                    if self.is_on_a_ladder():
                        self.dy = self.CLIMB_SPEED
                        self.dx = 0
                        self.state = self.State.CLIMBING
                if w.is_key_pressed('s'):
                    if self.is_on_a_ladder():
                        self.dy = -self.CLIMB_SPEED
                        self.dx = 0
                        self.state = self.State.CLIMBING

        elif self.state is self.State.STANDING:
            if not self.is_on_a_platform():
                self.state = self.State.FALLING
                self.dy = 0
            else:
                if w.is_key_down(' '):
                    self.state = self.State.JUMPING
                    self.dy = self.JUMP_VELOCITY
                if w.is_key_pressed('w'):
                    if self.is_on_bottom_of_ladder():
                        self.dy = self.CLIMB_SPEED
                        self.dx = 0
                        self.state = self.State.CLIMBING
                if w.is_key_pressed('s'):
                    if self.is_on_top_of_ladder():
                        self.dy = -self.CLIMB_SPEED
                        self.dx = 0
                        self.state = self.State.CLIMBING

        elif self.state is Player.State.CLIMBING:
            if not self.is_on_a_ladder():
                if self.is_on_a_platform():
                    self.state = self.State.STANDING
                    self.dy = 0
                else:
                    self.state = self.State.FALLING
            elif w.is_key_pressed('w'):
                self.dy = Player.CLIMB_SPEED
                if self.is_on_top_of_ladder() and self.is_on_a_platform():
                    self.state = Player.State.STANDING
            elif w.is_key_pressed('s'):
                self.dy = -Player.CLIMB_SPEED
                if self.is_on_bottom_of_ladder() and self.is_on_a_platform():
                    self.state = Player.State.STANDING
            else:
                self.dy = 0


w.create_sprite(Player)
w.run()
