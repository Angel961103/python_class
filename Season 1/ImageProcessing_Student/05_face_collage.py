import os
import random

from pycat.core import Window, Sprite, KeyCode
from pycat.base import NumpyImage as Image


def load_images(img_dir: str):
    face_images = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_dir_path = dir_path + "/" + img_dir
    for file in os.listdir(img_dir_path):
        filepath = img_dir_path + file
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            face_images.append(Image.get_array_from_file(img_dir + "/" + file))
    return face_images


def create_grid_collage(grid_rows, grid_cols, image_list) -> Sprite:
    img_rows, img_cols, img_channels = image_list[0].shape
    s = window.create_sprite()
    collage = Image(img_rows, img_cols, img_channels)
    di = img_rows/grid_rows
    dj = img_cols/grid_cols
    for i in range(grid_rows):
        for j in range(grid_cols):
            s = window.create_sprite()
            img = random.choice(image_list)
            i0, i1 = int(i*di), int((i+1)*di)
            j0, j1 = int(j*dj), int((j+1)*dj)
            collage[i0:i1, j0:j1, :] = img[i0:i1, j0:j1, :]
    s.texture = collage.texture
    return s


def create_row_collage(rows, image_list) -> Sprite:
    img_rows, img_cols, img_channels = image_list[0].shape
    di = img_rows/rows
    s = window.create_sprite()
    collage = Image(img_rows, img_cols, img_channels)
    for i in range(rows):
        img = random.choice(image_list)
        i0, i1 = int(i*di), int((i+1)*di)
        collage[i0:i1, :, :] = img[i0:i1, :, :]
    s.texture = collage.texture
    return s


def create_column_collage(grid_cols, image_list) -> Sprite:
    img_rows, img_cols, img_channels = image_list[0].shape
    dj = img_cols/grid_cols
    s = window.create_sprite()
    collage = Image(img_rows, img_cols, img_channels)
    for j in range(grid_cols):
        img = random.choice(image_list)
        j0, j1 = int(j*dj), int((j+1)*dj)
        collage[:, j0:j1, :] = img[:, j0:j1, :]
    s.texture = collage.texture
    return s


class CollageGenerator(Sprite):

    def on_create(self):
        self.is_visible = False

    def on_update(self, dt):
        if window.get_key_down(KeyCode._1):
            window.delete_sprites_with_tag("row")
            sprite = create_row_collage(7, face_images)
            sprite.position = (.2 * window.width, window.center.y)
            sprite.scale = 4
            sprite.add_tag("row")

        if window.get_key_down(KeyCode._2):
            window.delete_sprites_with_tag("grid")
            sprite = create_grid_collage(7, 7, face_images)
            sprite.position = window.center
            sprite.scale = 4
            sprite.add_tag("grid")

        if window.get_key_down(KeyCode._3):
            window.delete_sprites_with_tag("column")
            sprite = create_column_collage(7, face_images)
            sprite.position = (.8 * window.width, window.center.y)
            sprite.scale = 4
            sprite.add_tag("column")


face_images = load_images("resized_faces")
window = Window()
window.create_sprite(CollageGenerator)
window.run()
