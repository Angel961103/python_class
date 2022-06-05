from pycat.core import Window


def generate_level(w: Window, tag: str):
    w.create_sprite(x=365.0, y=228, scale_x=10, scale_y=340, tag=tag)
