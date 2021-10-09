import os
import cv2
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
img_dir_path = dir_path + "/resized_faces/"
faces = 0
average_image = None

for file in os.listdir(img_dir_path):
    filepath = img_dir_path + file
    if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        img = cv2.imread(filepath)
        if average_image is None:
            #  use astype(np.uint64) to avoid overflow
            average_image = img.astype(np.uint64)
        else:
            average_image += img.astype(np.uint64)
        faces += 1

if average_image is not None:
    average_image //= faces
    cv2.imwrite(dir_path+"/average_face.jpg", average_image.astype(np.uint8))
