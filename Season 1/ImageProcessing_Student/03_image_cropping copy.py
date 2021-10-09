from pycat.core import Window
from pycat.base import NumpyImage as Image
import os
import random

window = Window()
original_image = Image.get_array_from_file("average_face.jpg")
print(original_image.shape)
rows, cols, channels = original_image.shape

def load_images(img_dir: str):
    face_images = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_dir_path = dir_path + "/" + img_dir
    for file in os.listdir(img_dir_path):
        filepath = img_dir_path + file
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            face_images.append(Image.get_array_from_file(img_dir + "/" + file))
    return face_images

face_images = load_images("resized_faces")
original_image = random.choice(face_images)

image_sprite = window.create_sprite()
image_sprite.texture = Image.get_texture_from_array(original_image)
image_sprite.position = (400, 400)
original_image = random.choice(face_images)
left_eye_image = original_image[50:70, 25:40, :]
left_eye = window.create_sprite()
left_eye.position = (600, 500)
left_eye.texture = Image.get_texture_from_array(left_eye_image)
left_eye.scale = 3
original_image = random.choice(face_images)
right_eye_image = original_image[50:70, 55:70, :]
right_eye = window.create_sprite()
right_eye.position = (700, 500)
right_eye.texture = Image.get_texture_from_array(right_eye_image)
right_eye.scale = 3
original_image = random.choice(face_images)
nose_image = original_image[27:55, 30:65, :]
nose = window.create_sprite()
nose.position = (650, 400)
nose.texture = Image.get_texture_from_array(nose_image)
nose.scale = 2
original_image = random.choice(face_images)
mouth_image = original_image[10:30, 30:65, :]
mouth = window.create_sprite()
mouth.position = (650, 300)
mouth.texture = Image.get_texture_from_array(mouth_image)
mouth.scale = 2


# right_eye = window.create_sprite()
# nose = window.create_sprite()
# mouth = window.create_sprite()

window.run()