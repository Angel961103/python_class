from pycat.core import Window


def generate_level(w: Window, tag: str):
    w.create_sprite(x=365.5, y=370.0, scale_x=-201, scale_y=42, tag=tag)
    w.create_sprite(x=679.0, y=0, scale_x=-1350, scale_y=118, tag=tag)
    w.create_sprite(x=747.5, y=158.0, scale_x=-251, scale_y=40, tag=tag)
    w.create_sprite(x=1074.0, y=279.5, scale_x=-196, scale_y=39, tag=tag)
    w.create_sprite(x=762.0, y=423.0, scale_x=182, scale_y=46, tag=tag)
